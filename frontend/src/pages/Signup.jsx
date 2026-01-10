import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import Button from '../components/ui/Button'
import Input from '../components/ui/Input'
import { useToast } from '../components/ui/Toast'
import '../styles/Auth.css'

const Signup = () => {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [errors, setErrors] = useState({})
  const [touched, setTouched] = useState({})
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()
  const toast = useToast()

  const validateName = (name) => {
    if (!name) return 'Name is required'
    if (name.length < 2) return 'Name must be at least 2 characters'
    return ''
  }

  const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!email) return 'Email is required'
    if (!emailRegex.test(email)) return 'Please enter a valid email'
    return ''
  }

  const validatePassword = (password) => {
    if (!password) return 'Password is required'
    if (password.length < 6) return 'Password must be at least 6 characters'
    if (!/[A-Z]/.test(password)) return 'Password should include an uppercase letter'
    if (!/[0-9]/.test(password)) return 'Password should include a number'
    return ''
  }

  const validateConfirmPassword = (confirmPassword) => {
    if (!confirmPassword) return 'Please confirm your password'
    if (confirmPassword !== password) return 'Passwords do not match'
    return ''
  }

  const handleBlur = (field) => {
    setTouched(prev => ({ ...prev, [field]: true }))
    
    const validators = {
      name: () => validateName(name),
      email: () => validateEmail(email),
      password: () => validatePassword(password),
      confirmPassword: () => validateConfirmPassword(confirmPassword)
    }

    if (validators[field]) {
      setErrors(prev => ({ ...prev, [field]: validators[field]() }))
    }
  }

  const getPasswordStrength = () => {
    if (!password) return { strength: 0, label: '' }
    let strength = 0
    if (password.length >= 6) strength++
    if (password.length >= 10) strength++
    if (/[A-Z]/.test(password)) strength++
    if (/[0-9]/.test(password)) strength++
    if (/[^A-Za-z0-9]/.test(password)) strength++
    
    const labels = ['', 'Weak', 'Fair', 'Good', 'Strong', 'Very Strong']
    return { strength, label: labels[strength] }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    // Validate all fields
    const allErrors = {
      name: validateName(name),
      email: validateEmail(email),
      password: validatePassword(password),
      confirmPassword: validateConfirmPassword(confirmPassword)
    }
    
    setErrors(allErrors)
    setTouched({ name: true, email: true, password: true, confirmPassword: true })

    const hasErrors = Object.values(allErrors).some(error => error)
    if (hasErrors) {
      toast.error('Please fix the errors below')
      return
    }

    setLoading(true)

    try {
      await new Promise(resolve => setTimeout(resolve, 1000))
      localStorage.setItem('isAuthenticated', 'true')
      localStorage.setItem('userEmail', email)
      localStorage.setItem('userName', name)
      toast.success('Account created successfully!')
      navigate('/chat')
    } catch (err) {
      toast.error('Registration failed. Please try again.')
      setLoading(false)
    }
  }

  const passwordStrength = getPasswordStrength()

  return (
    <div className="auth-page">
      <div className="auth-container">
        <div className="auth-card">
          <div className="auth-header">
            <Link to="/" className="auth-logo" aria-label="Go to home page">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" aria-hidden="true">
                <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                <path d="M2 17l10 5 10-5"/>
                <path d="M2 12l10 5 10-5"/>
              </svg>
            </Link>
            <h1>Create Account</h1>
            <p>Sign up to start using Legal AI</p>
          </div>

          <form onSubmit={handleSubmit} className="auth-form" noValidate>
            <Input
              type="text"
              label="Full Name"
              name="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              onBlur={() => handleBlur('name')}
              placeholder="Enter your name"
              autoComplete="name"
              required
              error={touched.name ? errors.name : ''}
              icon={
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                  <circle cx="12" cy="7" r="4"/>
                </svg>
              }
            />

            <Input
              type="email"
              label="Email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              onBlur={() => handleBlur('email')}
              placeholder="Enter your email"
              autoComplete="email"
              required
              error={touched.email ? errors.email : ''}
              icon={
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                  <polyline points="22,6 12,13 2,6"/>
                </svg>
              }
            />

            <div className="password-field-wrapper">
              <Input
                type="password"
                label="Password"
                name="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                onBlur={() => handleBlur('password')}
                placeholder="Create a password"
                autoComplete="new-password"
                required
                error={touched.password ? errors.password : ''}
                hint={!touched.password && password ? `Strength: ${passwordStrength.label}` : ''}
                icon={
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
                  </svg>
                }
              />
              {password && !touched.password && (
                <div className="password-strength" role="meter" aria-valuenow={passwordStrength.strength} aria-valuemin="0" aria-valuemax="5">
                  <div className="strength-bars">
                    {[1, 2, 3, 4, 5].map(level => (
                      <div 
                        key={level} 
                        className={`strength-bar ${passwordStrength.strength >= level ? 'active' : ''}`}
                        style={{ backgroundColor: passwordStrength.strength >= level ? 
                          passwordStrength.strength <= 2 ? '#ef4444' : 
                          passwordStrength.strength <= 3 ? '#f59e0b' : '#10a37f' 
                          : undefined 
                        }}
                      />
                    ))}
                  </div>
                </div>
              )}
            </div>

            <Input
              type="password"
              label="Confirm Password"
              name="confirmPassword"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              onBlur={() => handleBlur('confirmPassword')}
              placeholder="Confirm your password"
              autoComplete="new-password"
              required
              error={touched.confirmPassword ? errors.confirmPassword : ''}
              success={touched.confirmPassword && !errors.confirmPassword && confirmPassword ? 'Passwords match!' : ''}
              icon={
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                </svg>
              }
            />

            <Button 
              type="submit" 
              variant="primary" 
              fullWidth 
              loading={loading}
              disabled={loading}
            >
              Create Account
            </Button>
          </form>

          <div className="auth-footer">
            <p>Already have an account? <Link to="/login">Log in</Link></p>
          </div>
        </div>

        <Link to="/" className="back-home">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
          </svg>
          Back to home
        </Link>
      </div>
    </div>
  )
}

export default Signup
