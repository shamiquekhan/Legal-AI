# 🚀 Free Deployment Guide - Legal AI RAG

Deploy your Legal AI RAG application completely FREE using Render (backend) and Vercel (frontend).

---

## Prerequisites

1. **GitHub Account** - Push your code to GitHub
2. **OpenAI API Key** - For the AI functionality
3. **Render Account** - https://render.com (free)
4. **Vercel Account** - https://vercel.com (free)

---

## Step 1: Push to GitHub

```bash
# Initialize git (if not already)
git init

# Add .gitignore
echo "venv/
node_modules/
__pycache__/
.env
*.pyc
.DS_Store
dist/
chroma_db/
*.log" > .gitignore

# Commit
git add .
git commit -m "Prepare for deployment"

# Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/legal-ai-rag.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy Backend to Render (FREE)

### Option A: One-Click Deploy (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **New** → **Web Service**
3. Connect your GitHub repository
4. Render will auto-detect `render.yaml`

### Option B: Manual Setup

1. **Create New Web Service**
   - Repository: Select your GitHub repo
   - Name: `legal-ai-backend`
   - Runtime: **Python 3**
   - Build Command: `pip install -r requirements-deploy.txt`
   - Start Command: `uvicorn src.main_standalone:app --host 0.0.0.0 --port $PORT`

2. **Environment Variables** (Add in Render Dashboard)
   ```
   OPENAI_API_KEY=sk-your-openai-api-key
   PYTHON_VERSION=3.11.0
   ```

3. **Plan**: Select **Free**

4. Click **Create Web Service**

5. Wait 5-10 minutes for deployment

6. Your backend URL will be: `https://legal-ai-backend.onrender.com`

### ⚠️ Free Tier Limitations
- Sleeps after 15 minutes of inactivity
- First request after sleep takes ~30 seconds (cold start)
- 512MB RAM limit

---

## Step 3: Deploy Frontend to Vercel (FREE)

### Option A: Vercel CLI (Fastest)

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to frontend
cd frontend

# Deploy
vercel

# Follow prompts:
# - Link to existing project? No
# - Project name: legal-ai-frontend
# - Directory: ./
# - Override settings? No
```

### Option B: Vercel Dashboard

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **Add New** → **Project**
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

5. **Environment Variables** (Add before deploying)
   ```
   VITE_API_URL=https://legal-ai-backend.onrender.com
   ```
   ⚠️ Replace with YOUR Render backend URL!

6. Click **Deploy**

7. Your frontend URL will be: `https://legal-ai-frontend.vercel.app`

---

## Step 4: Update Frontend Environment

After getting your Render backend URL, update the production environment:

1. In Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add/Update:
   ```
   VITE_API_URL = https://your-actual-backend-name.onrender.com
   ```
3. Redeploy the frontend

---

## 🔧 Troubleshooting

### Backend Issues

**"Application Error" on Render**
- Check logs in Render Dashboard
- Ensure OPENAI_API_KEY is set correctly
- Check if all dependencies are in requirements-deploy.txt

**Memory Limit Exceeded**
- Free tier has 512MB limit
- Use requirements-deploy.txt (lighter dependencies)
- Consider upgrading to paid tier ($7/month)

**Cold Start Slow**
- Free tier sleeps after 15min inactivity
- First request takes ~30 seconds
- Use a service like UptimeRobot to ping every 14 minutes

### Frontend Issues

**CORS Errors**
- Backend already has CORS enabled for all origins
- Check if VITE_API_URL is correct
- Ensure no trailing slash in URL

**API Not Connecting**
- Verify backend is running (check Render logs)
- Check browser console for errors
- Test backend health endpoint directly

---

## 📊 Alternative Free Hosting Options

### Backend Alternatives

| Service | Free Tier | Pros | Cons |
|---------|-----------|------|------|
| **Railway** | $5 credit/month | Fast, no cold starts | Credit runs out |
| **Fly.io** | 3 shared VMs | Fast, global | More complex setup |
| **Koyeb** | 1 nano instance | No cold starts | Limited resources |
| **Hugging Face Spaces** | Unlimited | Good for ML | Gradio/Streamlit only |

### Frontend Alternatives

| Service | Free Tier |
|---------|-----------|
| **Netlify** | Unlimited sites |
| **Cloudflare Pages** | Unlimited sites |
| **GitHub Pages** | Unlimited (static only) |

---

## 🔒 Production Security Checklist

- [ ] Remove `allow_origins=["*"]` and specify your frontend domain
- [ ] Use environment variables for all secrets
- [ ] Enable HTTPS (automatic on Render/Vercel)
- [ ] Add rate limiting
- [ ] Set up monitoring/alerts

---

## 📈 Scaling Beyond Free Tier

When ready to scale:

1. **Render Starter** ($7/month) - No cold starts, more RAM
2. **Vercel Pro** ($20/month) - Faster builds, analytics
3. **Railway** ($5-20/month) - Usage-based pricing
4. **DigitalOcean App Platform** ($5/month) - Good value

---

## Quick Reference

```
Backend URL:  https://legal-ai-backend.onrender.com
Frontend URL: https://legal-ai-frontend.vercel.app
Health Check: https://legal-ai-backend.onrender.com/health
API Endpoint: https://legal-ai-backend.onrender.com/api/v1/query/legal
```

Replace with your actual URLs after deployment!
