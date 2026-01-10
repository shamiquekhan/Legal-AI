import './LoadingSpinner.css'

const LoadingSpinner = ({ size = 'md', color = 'primary', text = '' }) => {
  const sizeClasses = {
    sm: 'spinner-sm',
    md: 'spinner-md',
    lg: 'spinner-lg'
  }

  return (
    <div className="loading-spinner-container" role="status" aria-live="polite">
      <div 
        className={`loading-spinner ${sizeClasses[size]} spinner-${color}`}
        aria-hidden="true"
      />
      {text && <span className="spinner-text">{text}</span>}
      <span className="sr-only">Loading...</span>
    </div>
  )
}

export default LoadingSpinner
