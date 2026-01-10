import { Link } from 'react-router-dom'
import { useState, useEffect } from 'react'
import DocumentSearchAnimation from '../components/animations/DocumentSearchAnimation'
import Button from '../components/ui/Button'
import '../styles/LandingPage.css'

const LandingPage = () => {
  const [isLoaded, setIsLoaded] = useState(false)

  useEffect(() => {
    setIsLoaded(true)
  }, [])

  const features = [
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          <path d="M9 12l2 2 4-4"/>
        </svg>
      ),
      title: "100% Accurate",
      description: "Zero-hallucination responses backed by authentic Indian legal sources. Every answer is verified."
    },
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
          <circle cx="12" cy="12" r="10"/>
          <polyline points="12,6 12,12 16,14"/>
        </svg>
      ),
      title: "Instant Answers",
      description: "Get legal information in milliseconds. No more hours of research or expensive consultations."
    },
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
        </svg>
      ),
      title: "Complete Coverage",
      description: "IPC, Constitution, CrPC, and more. Comprehensive knowledge of Indian law at your fingertips."
    },
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
        </svg>
      ),
      title: "Natural Conversation",
      description: "Ask questions in plain English or Hindi. Our AI understands context and legal terminology."
    },
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
          <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
          <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
        </svg>
      ),
      title: "Private & Secure",
      description: "Your queries are confidential. No data sharing, no tracking, just secure legal assistance."
    },
    {
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
          <path d="M12 2L2 7l10 5 10-5-10-5z"/>
          <path d="M2 17l10 5 10-5"/>
          <path d="M2 12l10 5 10-5"/>
        </svg>
      ),
      title: "Step-by-Step Guidance",
      description: "Get practical procedures and actionable steps, not just legal definitions."
    }
  ]

  const stats = [
    { value: "125+", label: "Legal Topics Covered" },
    { value: "100%", label: "Accuracy Rate" },
    { value: "<50ms", label: "Response Time" },
    { value: "24/7", label: "Availability" }
  ]

  const legalAreas = [
    "IPC Sections 302-307 (Murder & Assault)",
    "Constitutional Articles 14-32 (Fundamental Rights)",
    "Bail & Arrest Procedures",
    "Domestic Violence Act 2005",
    "Cheating & Fraud Laws (IPC 420)",
    "Self-Defense Rights",
    "FIR Filing Procedures",
    "And many more..."
  ]

  const ArrowIcon = () => (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
      <path d="M5 12h14M12 5l7 7-7 7"/>
    </svg>
  )

  return (
    <div className={`landing-page ${isLoaded ? 'loaded' : ''}`}>
      {/* Skip to main content link for accessibility */}
      <a href="#main-content" className="skip-link">
        Skip to main content
      </a>

      {/* Navigation */}
      <nav className="landing-nav" role="navigation" aria-label="Main navigation">
        <div className="nav-container">
          <Link to="/" className="nav-logo" aria-label="Legal AI Home">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
              <path d="M12 2L2 7l10 5 10-5-10-5z"/>
              <path d="M2 17l10 5 10-5"/>
              <path d="M2 12l10 5 10-5"/>
            </svg>
            <span>Legal AI</span>
          </Link>
          <div className="nav-links" role="menubar">
            <a href="#features" role="menuitem">Features</a>
            <a href="#how-it-works" role="menuitem">How It Works</a>
            <a href="#coverage" role="menuitem">Coverage</a>
            <a href="#about" role="menuitem">About</a>
          </div>
          <div className="nav-actions">
            <Button as={Link} to="/login" variant="ghost" size="sm">
              Log In
            </Button>
            <Button as={Link} to="/signup" variant="primary" size="sm">
              Sign Up Free
            </Button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <main id="main-content">
        <section className="hero" aria-labelledby="hero-title">
          <div className="hero-bg" aria-hidden="true"></div>
          <div className="hero-container">
            <div className="hero-content">
              <div className="hero-badge" role="status">
                <span className="badge-dot" aria-hidden="true"></span>
                Zero-Hallucination Legal AI
              </div>
              <h1 id="hero-title" className="hero-title">
                Understanding
                <span className="gradient-text">Indian Law</span>
                Made Simple
              </h1>
              <p className="hero-subtitle">
                Get instant, reliable answers to your legal questions. Powered by AI that never guesses—only
                speaks when it has proof from authentic Indian legal sources.
              </p>
              <div className="hero-cta">
                <Button 
                  as={Link} 
                  to="/signup" 
                  variant="primary" 
                  size="lg"
                  iconRight={<ArrowIcon />}
                >
                  Start Free
                </Button>
                <Button 
                  as={Link} 
                  to="/login" 
                  variant="secondary" 
                  size="lg"
                >
                  Log In
                </Button>
              </div>
            </div>
            
            {/* Stats Grid */}
            <div className="hero-stats" role="list" aria-label="Key statistics">
              {stats.map((stat, index) => (
                <div key={index} className="stat-item" role="listitem">
                  <span className="stat-value">{stat.value}</span>
                  <span className="stat-label">{stat.label}</span>
                  <span className="sr-only">{stat.value} {stat.label}</span>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section id="features" className="features-section" aria-labelledby="features-title">
          <div className="section-container">
            <div className="section-header">
              <span className="section-label">Features</span>
              <h2 id="features-title" className="section-title">Why Choose Legal AI?</h2>
              <p className="section-subtitle">
                Built specifically for Indian law, our AI provides accurate, actionable legal information.
              </p>
            </div>
            
            <div className="features-grid" role="list">
              {features.map((feature, index) => (
                <article 
                  key={index} 
                  className="feature-card"
                  role="listitem"
                  style={{ animationDelay: `${index * 0.1}s` }}
                >
                  <div className="feature-icon" aria-hidden="true">{feature.icon}</div>
                  <h3>{feature.title}</h3>
                  <p>{feature.description}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* How It Works Section - Document Search Animation */}
        <section id="how-it-works" className="how-it-works-section" aria-labelledby="how-it-works-title">
          <div className="section-container">
            <div className="section-header">
              <span className="section-label">How It Works</span>
              <h2 id="how-it-works-title" className="section-title">AI-Powered Legal Research</h2>
              <p className="section-subtitle">
                Watch how our AI searches through authentic legal documents to find accurate answers.
              </p>
            </div>
            
            <DocumentSearchAnimation />
          </div>
        </section>

        {/* Coverage Section */}
        <section id="coverage" className="coverage-section" aria-labelledby="coverage-title">
          <div className="section-container">
            <div className="coverage-content">
              <div className="coverage-text">
                <span className="section-label">Legal Coverage</span>
                <h2 id="coverage-title" className="section-title">Comprehensive Indian Law Knowledge</h2>
                <p className="section-subtitle">
                  From criminal law to constitutional rights, get accurate information on a wide range of legal topics.
                </p>
                <ul className="coverage-list" role="list" aria-label="Legal areas covered">
                  {legalAreas.map((area, index) => (
                    <li key={index} role="listitem">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
                        <path d="M20 6L9 17l-5-5"/>
                      </svg>
                      {area}
                    </li>
                  ))}
                </ul>
                <Button 
                  as={Link} 
                  to="/signup" 
                  variant="ghost"
                  iconRight={
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
                      <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                  }
                  className="coverage-cta"
                >
                  Explore All Topics
                </Button>
              </div>
              <div className="coverage-visual" aria-hidden="true">
                <div className="code-demo">
                  <div className="demo-header">
                    <span className="demo-dot red"></span>
                    <span className="demo-dot yellow"></span>
                    <span className="demo-dot green"></span>
                    <span className="demo-title">Legal AI Chat</span>
                  </div>
                  <div className="demo-body">
                    <div className="demo-message user">
                      <span className="demo-label">You</span>
                      <p>What are my rights if I'm arrested?</p>
                    </div>
                    <div className="demo-message ai">
                      <span className="demo-label">Legal AI</span>
                      <p>
                        <strong>Your Rights Upon Arrest:</strong><br/>
                        ✓ Right to know grounds of arrest (Art. 22)<br/>
                        ✓ Right to legal counsel immediately<br/>
                        ✓ Right to inform family/friend<br/>
                        ✓ Must be produced before magistrate within 24 hours<br/>
                        ✓ Right against self-incrimination
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section id="about" className="cta-section" aria-labelledby="cta-title">
          <div className="section-container">
            <div className="cta-content">
              <h2 id="cta-title">Ready to Get Legal Answers?</h2>
              <p>
                Join thousands of users who trust Legal AI for accurate Indian legal information.
                Sign up now and get instant access to our AI-powered legal assistant.
              </p>
              <div className="cta-buttons">
                <Button 
                  as={Link} 
                  to="/signup" 
                  variant="primary" 
                  size="lg"
                  iconRight={<ArrowIcon />}
                >
                  Create Free Account
                </Button>
              </div>
              <p className="cta-note">No credit card required. Free forever for basic use.</p>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="landing-footer" role="contentinfo">
        <div className="footer-container">
          <div className="footer-brand">
            <div className="footer-logo">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
                <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                <path d="M2 17l10 5 10-5"/>
                <path d="M2 12l10 5 10-5"/>
              </svg>
              <span>Legal AI</span>
            </div>
            <p>AI-powered Indian legal assistance with zero hallucination.</p>
          </div>
          <div className="footer-links">
            <div className="footer-column">
              <h4>Product</h4>
              <a href="#features">Features</a>
              <a href="#how-it-works">How It Works</a>
              <a href="#coverage">Coverage</a>
              <Link to="/signup">Sign Up</Link>
            </div>
            <div className="footer-column">
              <h4>Connect</h4>
              <a href="https://github.com/shamiquekhan" target="_blank" rel="noopener noreferrer">GitHub</a>
              <a href="https://www.linkedin.com/in/shamique-khan" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>© 2026 Legal AI by <a href="https://github.com/shamiquekhan" target="_blank" rel="noopener noreferrer">Shamique Khan</a>. This is an AI assistant and does not constitute legal advice.</p>
        </div>
      </footer>
    </div>
  )
}

export default LandingPage
