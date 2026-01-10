import { useEffect, useRef, useState } from 'react'
import './DocumentSearchAnimation.css'

const DocumentSearchAnimation = () => {
  const [isVisible, setIsVisible] = useState(false)
  const containerRef = useRef(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true)
        }
      },
      { threshold: 0.3 }
    )

    if (containerRef.current) {
      observer.observe(containerRef.current)
    }

    return () => observer.disconnect()
  }, [])

  return (
    <div 
      ref={containerRef}
      className={`doc-search-animation ${isVisible ? 'visible' : ''}`}
      role="img"
      aria-label="Animation showing document search process: upload documents, AI analyzes them, and provides legal answers"
    >
      {/* Process Steps */}
      <div className="process-flow">
        {/* Step 1: Document Upload */}
        <div className="process-step step-1">
          <div className="step-icon document-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/>
              <path d="M14 2v6h6"/>
              <path d="M16 13H8M16 17H8M10 9H8"/>
            </svg>
            <div className="doc-lines">
              <span className="line"></span>
              <span className="line"></span>
              <span className="line"></span>
            </div>
          </div>
          <span className="step-label">Legal Documents</span>
        </div>

        {/* Connector 1 */}
        <div className="connector">
          <div className="connector-line"></div>
          <div className="connector-arrow"></div>
        </div>

        {/* Step 2: AI Analysis with Magnifying Glass */}
        <div className="process-step step-2">
          <div className="step-icon search-icon">
            <div className="magnifying-glass">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="11" cy="11" r="8"/>
                <path d="M21 21l-4.35-4.35"/>
              </svg>
            </div>
            <div className="scan-beam"></div>
            <div className="data-particles">
              <span className="particle"></span>
              <span className="particle"></span>
              <span className="particle"></span>
              <span className="particle"></span>
            </div>
          </div>
          <span className="step-label">AI Analysis</span>
        </div>

        {/* Connector 2 */}
        <div className="connector">
          <div className="connector-line"></div>
          <div className="connector-arrow"></div>
        </div>

        {/* Step 3: Results */}
        <div className="process-step step-3">
          <div className="step-icon result-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
              <path d="M9 12l2 2 4-4"/>
            </svg>
            <div className="checkmark-pulse"></div>
          </div>
          <span className="step-label">Verified Answer</span>
        </div>
      </div>

      {/* Background Elements */}
      <div className="bg-grid" aria-hidden="true">
        {Array.from({ length: 20 }).map((_, i) => (
          <div key={i} className="grid-dot" style={{ '--i': i }} />
        ))}
      </div>
    </div>
  )
}

export default DocumentSearchAnimation
