import { useState, useRef, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useToast } from '../components/ui/Toast'
import LoadingSpinner from '../components/ui/LoadingSpinner'
import '../App.css'
import '../styles/Chat.css'

function Chat() {
  const [query, setQuery] = useState('')
  const [messages, setMessages] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [isConnected, setIsConnected] = useState(false)
  const [isCheckingConnection, setIsCheckingConnection] = useState(true)
  const messagesEndRef = useRef(null)
  const textareaRef = useRef(null)
  const navigate = useNavigate()
  const toast = useToast()

  // Use environment variable for API URL (for deployment)
  const API_BASE = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8002'
  const API_URL = `${API_BASE}/api/v1/query/legal`

  useEffect(() => {
    // Check if user is authenticated
    const isAuthenticated = localStorage.getItem('isAuthenticated')
    if (!isAuthenticated) {
      navigate('/login')
      return
    }
    checkConnection()
  }, [navigate])

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto'
      textareaRef.current.style.height = Math.min(textareaRef.current.scrollHeight, 200) + 'px'
    }
  }, [query])

  const checkConnection = async () => {
    setIsCheckingConnection(true)
    try {
      const response = await fetch(`${API_BASE}/health`)
      if (response.ok) {
        setIsConnected(true)
        toast.success('Connected to Legal AI server')
      } else {
        setIsConnected(false)
        toast.warning('Server is not responding properly')
      }
    } catch {
      setIsConnected(false)
      toast.error('Could not connect to server. Please ensure the backend is running.')
    } finally {
      setIsCheckingConnection(false)
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!query.trim() || isLoading) return

    const userMessage = query.trim()
    setQuery('')
    if (textareaRef.current) textareaRef.current.style.height = 'auto'
    
    setMessages(prev => [...prev, { type: 'user', content: userMessage }])
    setIsLoading(true)

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: userMessage })
      })

      if (!response.ok) throw new Error('Server error')
      const data = await response.json()
      
      setMessages(prev => [...prev, {
        type: 'assistant',
        content: data.answer,
        confidence: data.confidence,
        processingTime: data.processing_time_ms
      }])
    } catch (error) {
      setMessages(prev => [...prev, {
        type: 'error',
        content: 'Unable to connect. Please ensure the server is running on port 8002.'
      }])
      toast.error('Failed to get response. Please try again.')
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e)
    }
  }

  const clearChat = () => {
    setMessages([])
    toast.info('Chat cleared')
  }

  const handleLogout = () => {
    localStorage.removeItem('isAuthenticated')
    localStorage.removeItem('userEmail')
    localStorage.removeItem('userName')
    toast.success('Logged out successfully')
    navigate('/')
  }

  const suggestedQueries = [
    { icon: "⚖️", title: "Murder Punishment", query: "What is the punishment for murder under IPC?" },
    { icon: "📜", title: "Fundamental Rights", query: "Explain Article 21 of the Constitution" },
    { icon: "🔍", title: "Cheating Laws", query: "What is IPC Section 420?" },
    { icon: "🛡️", title: "Arrest Rights", query: "What are my rights if arrested?" }
  ]

  const userName = localStorage.getItem('userName') || localStorage.getItem('userEmail')?.split('@')[0] || 'User'

  return (
    <div className="app" role="application" aria-label="Legal AI Chat">
      {/* Skip to main content */}
      <a href="#chat-input" className="skip-link">Skip to chat input</a>

      {/* Sidebar */}
      <aside className="sidebar" role="complementary" aria-label="Chat navigation">
        <div className="sidebar-header">
          <button 
            className="new-chat-btn" 
            onClick={clearChat}
            aria-label="Start a new chat"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
              <path d="M12 5v14M5 12h14"/>
            </svg>
            New chat
          </button>
        </div>
        
        <div className="sidebar-content">
          {messages.length > 0 && (
            <div className="chat-history" role="list" aria-label="Chat history">
              <span className="history-label">Today</span>
              <div className="history-item active" role="listitem">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
                  <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>
                </svg>
                <span>{messages[0]?.content?.slice(0, 30)}...</span>
              </div>
            </div>
          )}
        </div>
        
        <div className="sidebar-footer">
          <div 
            className={`status-indicator ${isCheckingConnection ? 'checking' : isConnected ? 'online' : 'offline'}`}
            role="status"
            aria-live="polite"
          >
            {isCheckingConnection ? (
              <LoadingSpinner size="sm" color="gray" />
            ) : (
              <span className="status-dot" aria-hidden="true"></span>
            )}
            <span>
              {isCheckingConnection ? 'Connecting...' : isConnected ? 'Server Online' : 'Disconnected'}
            </span>
          </div>
          <button 
            className="logout-btn" 
            onClick={handleLogout}
            aria-label="Log out of your account"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
              <path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4"/>
              <polyline points="16,17 21,12 16,7"/>
              <line x1="21" y1="12" x2="9" y2="12"/>
            </svg>
            <span>Log out</span>
          </button>
        </div>
      </aside>

      {/* Main Area */}
      <main className="main" role="main">
        <div className="chat-container">
          {messages.length === 0 ? (
            <div className="welcome">
              <div className="logo-container">
                <div className="logo" aria-hidden="true">
                  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                    <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                    <path d="M2 17l10 5 10-5"/>
                    <path d="M2 12l10 5 10-5"/>
                  </svg>
                </div>
              </div>
              <h1>Legal AI</h1>
              <p className="subtitle">Welcome, {userName}!</p>
              
              <div className="suggestions" role="list" aria-label="Suggested questions">
                {suggestedQueries.map((sq, i) => (
                  <button 
                    key={i} 
                    className="suggestion-btn"
                    onClick={() => setQuery(sq.query)}
                    role="listitem"
                    aria-label={`Ask: ${sq.query}`}
                  >
                    <span className="suggestion-icon" aria-hidden="true">{sq.icon}</span>
                    <div className="suggestion-text">
                      <span className="suggestion-title">{sq.title}</span>
                      <span className="suggestion-query">{sq.query}</span>
                    </div>
                    <svg className="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
                      <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="messages" role="log" aria-label="Chat messages" aria-live="polite">
              {messages.map((msg, idx) => (
                <div key={idx} className={`message ${msg.type}`} role="article">
                  <div className="message-inner">
                    <div className="avatar" aria-hidden="true">
                      {msg.type === 'user' ? (
                        <div className="avatar-user">{userName.charAt(0).toUpperCase()}</div>
                      ) : (
                        <div className="avatar-ai">
                          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                            <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                            <path d="M2 17l10 5 10-5"/>
                            <path d="M2 12l10 5 10-5"/>
                          </svg>
                        </div>
                      )}
                    </div>
                    <div className="message-body">
                      <div className="message-sender">
                        {msg.type === 'user' ? 'You' : 'Legal AI'}
                      </div>
                      <div className="message-text">
                        {msg.type === 'user' ? (
                          <p>{msg.content}</p>
                        ) : msg.type === 'error' ? (
                          <p className="error-msg">{msg.content}</p>
                        ) : (
                          <>
                            <FormattedAnswer content={msg.content} />
                            <div className="message-footer">
                              <span>{msg.processingTime?.toFixed(0)}ms</span>
                              <span>•</span>
                              <span>{(msg.confidence * 100).toFixed(0)}% confidence</span>
                            </div>
                          </>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              ))}
              
              {isLoading && (
                <div className="message assistant">
                  <div className="message-inner">
                    <div className="avatar">
                      <div className="avatar-ai">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                          <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                          <path d="M2 17l10 5 10-5"/>
                          <path d="M2 12l10 5 10-5"/>
                        </svg>
                      </div>
                    </div>
                    <div className="message-body">
                      <div className="message-sender">Legal AI</div>
                      <div className="typing-indicator">
                        <span></span><span></span><span></span>
                      </div>
                    </div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>
          )}
        </div>

        {/* Input */}
        <div className="input-container">
          <form className="input-form" onSubmit={handleSubmit}>
            <div className="input-box">
              <textarea
                ref={textareaRef}
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Ask about Indian law..."
                rows="1"
                disabled={isLoading}
              />
              <button type="submit" disabled={!query.trim() || isLoading}>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
                </svg>
              </button>
            </div>
            <p className="footer-note">
              For educational purposes only. Consult a qualified lawyer for legal advice.
            </p>
          </form>
        </div>
      </main>
    </div>
  )
}

function FormattedAnswer({ content }) {
  if (!content) return null
  
  const cleanContent = content
    .replace(/[📚⚖️🔍💡⚠️❌✅🏛️📋🎯💾🚀📊🔥🏆📁📈📝🔧🚨]/g, '')
    .trim()
  
  const lines = cleanContent.split('\n').filter(l => l.trim())
  const elements = []
  let listItems = []
  let listKey = 0
  
  const flushList = () => {
    if (listItems.length > 0) {
      elements.push(
        <ul key={`list-${listKey++}`} className="answer-list">
          {listItems.map((item, j) => (
            <li key={j}>{parseInline(item)}</li>
          ))}
        </ul>
      )
      listItems = []
    }
  }
  
  const parseInline = (text) => {
    const parts = text.split(/(\*\*[^*]+\*\*)/g)
    return parts.map((part, i) => {
      if (part.startsWith('**') && part.endsWith('**')) {
        return <strong key={i}>{part.slice(2, -2)}</strong>
      }
      return part
    })
  }
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim()
    
    if (!line) continue
    
    if (line.match(/^\*\*[A-Z][A-Z\s:]+\*\*$/) || line.match(/^[A-Z][A-Z\s:]+$/)) {
      flushList()
      const text = line.replace(/\*\*/g, '').replace(/:$/, '')
      elements.push(<h3 key={i} className="section-title">{text}</h3>)
      continue
    }
    
    if (line.match(/^\*\*[^*]+\*\*:?/)) {
      flushList()
      const match = line.match(/^\*\*([^*]+)\*\*:?\s*(.*)/)
      if (match) {
        if (match[2]) {
          elements.push(
            <div key={i} className="info-row">
              <span className="info-label">{match[1]}</span>
              <span className="info-value">{match[2]}</span>
            </div>
          )
        } else {
          elements.push(<h4 key={i} className="subsection-title">{match[1]}</h4>)
        }
      }
      continue
    }
    
    if (line.match(/^(IPC|CrPC|Article)\s+(Section\s+)?\d+/i)) {
      flushList()
      elements.push(<div key={i} className="legal-reference">{line}</div>)
      continue
    }
    
    if (line.match(/^[•\-\*]\s/)) {
      listItems.push(line.replace(/^[•\-\*]\s*/, ''))
      continue
    }
    
    if (line.match(/^\d+\.\s/)) {
      listItems.push(line.replace(/^\d+\.\s*/, ''))
      continue
    }
    
    if (line.match(/Case:/i) || line.match(/v\.\s+(State|Union)/i)) {
      flushList()
      elements.push(
        <div key={i} className="case-cite">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/>
            <path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>
          </svg>
          <span>{parseInline(line)}</span>
        </div>
      )
      continue
    }
    
    if (line.match(/DISCLAIMER/i)) {
      flushList()
      elements.push(
        <div key={i} className="disclaimer-box">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 16v-4M12 8h.01"/>
          </svg>
          <span>{line.replace(/\*\*/g, '').replace('DISCLAIMER:', '').trim()}</span>
        </div>
      )
      continue
    }
    
    if (line.match(/Police:|Helpline:|1091|100/)) {
      flushList()
      elements.push(
        <div key={i} className="emergency-box">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/>
          </svg>
          <span>{line}</span>
        </div>
      )
      continue
    }
    
    flushList()
    elements.push(<p key={i} className="answer-para">{parseInline(line)}</p>)
  }
  
  flushList()
  return <div className="formatted-answer">{elements}</div>
}

export default Chat
