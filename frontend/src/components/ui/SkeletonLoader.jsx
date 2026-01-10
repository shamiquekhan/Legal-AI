import './SkeletonLoader.css'

const SkeletonLoader = ({ 
  type = 'text', 
  width = '100%', 
  height = '20px',
  count = 1,
  className = ''
}) => {
  const types = {
    text: 'skeleton-text',
    circle: 'skeleton-circle',
    rect: 'skeleton-rect',
    card: 'skeleton-card'
  }

  if (count > 1) {
    return (
      <div className={`skeleton-group ${className}`} role="status" aria-busy="true">
        {Array.from({ length: count }).map((_, i) => (
          <div
            key={i}
            className={`skeleton ${types[type]}`}
            style={{ width, height, '--delay': `${i * 0.1}s` }}
            aria-hidden="true"
          />
        ))}
        <span className="sr-only">Loading content...</span>
      </div>
    )
  }

  return (
    <div 
      className={`skeleton ${types[type]} ${className}`}
      style={{ width, height }}
      role="status"
      aria-busy="true"
    >
      <span className="sr-only">Loading...</span>
    </div>
  )
}

// Feature card skeleton
export const FeatureCardSkeleton = () => (
  <div className="skeleton-feature-card" role="status" aria-busy="true">
    <div className="skeleton skeleton-circle" style={{ width: '48px', height: '48px' }} />
    <div className="skeleton skeleton-text" style={{ width: '60%', height: '24px', marginTop: '16px' }} />
    <div className="skeleton skeleton-text" style={{ width: '100%', height: '16px', marginTop: '12px' }} />
    <div className="skeleton skeleton-text" style={{ width: '80%', height: '16px', marginTop: '8px' }} />
    <span className="sr-only">Loading feature...</span>
  </div>
)

export default SkeletonLoader
