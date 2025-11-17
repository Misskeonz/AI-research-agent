# 📦 Installation Guide

## Step-by-Step Setup Instructions

### Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher installed
- pip package manager
- OpenRouter API key (free from https://openrouter.ai)
- 500MB+ free disk space
- Modern web browser

---

## 🚀 Installation Steps

### Step 1: Download the Project

```bash
# Navigate to your desired directory
cd ~/projects

# Clone or extract the research_agent_flask folder
# If you have it as a ZIP file:
unzip research_agent_flask.zip
cd research_agent_flask
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 4: Configure Environment

1. Open `.env` file in text editor
2. Update these variables:

```bash
# IMPORTANT: Add your OpenRouter API key
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# For production, generate a new SECRET_KEY:
# (Run: python -c "import os; print(os.urandom(24).hex())")
SECRET_KEY=your-generated-key-here

# Optional: Change port if 5000 is in use
FLASK_PORT=5000
```

### Step 5: Initialize Database

The database will auto-initialize on first run, but you can pre-create it:

```bash
# Start the application (this creates the database)
python run.py

# Or manually with Python:
python -c "from app import init_db, app; app.app_context().push(); init_db()"
```

### Step 6: Start the Application

```bash
# Using run.py (recommended)
python run.py

# Or directly:
python app.py
```

You should see:

```
╔═══════════════════════════════════════════════════════╗
║   🤖 AI Research Agent Flask Application              ║
║                                                       ║
║   Starting server...                                  ║
║   Host: 0.0.0.0                                       
║   Port: 5000                                          
║   Debug: True                                         
║                                                       ║
║   🌐 Open: http://localhost:5000                      
║   📧 Login: admin / admin123                          
║                                                       ║
║   Press CTRL+C to stop                                ║
╚═══════════════════════════════════════════════════════╝
```

### Step 7: Access the Application

1. Open browser and go to: `http://localhost:5000`
2. Login with default credentials:
   - **Username:** `admin`
   - **Password:** `admin123`
3. ⚠️ Change admin password immediately!
   - Go to Settings → Change Password

---

## ✅ Verification Checklist

After installation, verify everything works:

- [ ] Application starts without errors
- [ ] Can access login page at http://localhost:5000
- [ ] Can login with admin/admin123
- [ ] Dashboard loads with no errors
- [ ] Can execute a test query
- [ ] Query processes and shows reasoning
- [ ] Can export query as TXT/PDF/DOC
- [ ] Can view query history
- [ ] Can access admin dashboard
- [ ] Can view user statistics

---

## 🐛 Common Installation Issues

### Issue: "Python not found"

```bash
# Check Python version
python --version
# or
python3 --version

# If neither works, install Python from:
# https://www.python.org/downloads/
```

### Issue: "ModuleNotFoundError: No module named 'flask'"

```bash
# Ensure virtual environment is activated
# Then reinstall requirements
pip install -r requirements.txt

# Or install specific package
pip install Flask==2.3.3
```

### Issue: "Port 5000 already in use"

```bash
# Option 1: Use different port
# Edit .env file and change:
FLASK_PORT=5001

# Option 2: Kill process using port 5000
# On macOS/Linux:
lsof -ti:5000 | xargs kill -9

# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Issue: "Database locked" error

```bash
# Remove old database and let it recreate
rm research_agent.db
python run.py
```

### Issue: "OpenRouter API Error"

```bash
# Verify API key
1. Go to https://openrouter.ai/dashboard
2. Copy your API key
3. Update .env file with correct key
4. Restart application
```

### Issue: "Export not working"

```bash
# Install missing package
pip install python-docx reportlab

# Then try exporting again
```

---

## 🔑 API Key Setup

### Get Your OpenRouter API Key

1. Visit https://openrouter.ai/signup
2. Create account or login
3. Go to Dashboard → Keys
4. Create new API key
5. Copy the key starting with `sk-or-v1-`

### Add to .env

```bash
# Open .env file
OPENROUTER_API_KEY=sk-or-v1-your-full-key-here
```

### Verify API Key Works

```bash
# Make a test request
curl -X GET "https://openrouter.ai/api/v1/auth/key/limits" \
  -H "Authorization: Bearer sk-or-v1-your-key-here"
```

---

## 📁 Project Structure After Setup

```
research_agent_flask/
├── venv/                      # Virtual environment
├── app.py                     # Main application
├── run.py                     # Easy launcher
├── requirements.txt           # Dependencies
├── .env                       # Configuration (keep secret!)
├── research_agent.db          # SQLite database (created on first run)
├── README.md                  # Documentation
├── templates/                 # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── history.html
│   ├── query_detail.html
│   ├── settings.html
│   ├── error.html
│   └── admin/
│       ├── dashboard.html
│       ├── users.html
│       ├── queries.html
│       └── user_queries.html
└── static/                    # CSS, JS, images
```

---

## 🔒 Security Setup

### For Production Deployment

1. **Change SECRET_KEY:**
   ```bash
   python -c "import os; print(os.urandom(24).hex())"
   # Copy output to .env SECRET_KEY
   ```

2. **Disable Debug Mode:**
   ```bash
   FLASK_DEBUG=False
   FLASK_ENV=production
   ```

3. **Change Admin Password:**
   - Login as admin
   - Go to Settings
   - Change password to something strong

4. **Setup HTTPS:**
   - Get SSL certificate
   - Configure web server
   - Use reverse proxy (Nginx/Apache)

5. **Database Security:**
   - Move database outside web root
   - Set proper file permissions
   - Regular backups

---

## 📚 Next Steps

After successful installation:

1. **Create User Account**
   - Register a new account
   - Test query functionality

2. **Execute First Query**
   - Go to Dashboard
   - Enter a research query
   - Wait for processing
   - View results with reasoning

3. **Explore Features**
   - View query history
   - Test export formats
   - Check admin dashboard
   - Manage user accounts

4. **Customize (Optional)**
   - Update branding
   - Adjust colors in base.html
   - Configure API settings

---

## 🚢 Deployment

### Local Network Access

```bash
# Change FLASK_HOST in .env to access from other devices
FLASK_HOST=0.0.0.0
# Then access from: http://your-ip:5000
```

### Cloud Deployment

**Heroku:**
```bash
heroku login
heroku create your-app-name
heroku config:set OPENROUTER_API_KEY=your-key
git push heroku main
```

**Railway/Render:**
- Connect GitHub repo
- Add environment variables
- Deploy automatically

---

## 📞 Support

If you encounter issues:

1. Check error messages in terminal
2. Review `.env` configuration
3. Verify API key is valid
4. Check internet connection
5. Review logs in application

---

## ✨ You're All Set!

Your AI Research Agent is ready to use! 🎉

**Default Admin Access:**
- URL: http://localhost:5000
- Username: admin
- Password: admin123

**Remember:** Change the admin password on first login!

Happy researching! 🚀
