# 🚀 Getting Started - Setup Checklist

Your **AI Research Agent Flask Application** is ready! Follow these steps to get it running.

---

## 📦 What You Have

A complete, production-ready Flask web application with:
- ✅ User authentication & admin panel
- ✅ AI research query execution with reasoning display
- ✅ Multi-format export (TXT, PDF, DOC)
- ✅ SQLite database
- ✅ Beautiful responsive UI
- ✅ Comprehensive documentation

**Total files:** 19+ HTML templates + Python app + Configuration

---

## ⚡ 5-Minute Quick Start

### Step 1: Navigate to the project
```bash
cd research_agent_flask
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

This installs all required packages (Flask, SQLAlchemy, OpenAI client, ReportLab, etc.)

### Step 3: Set your API key
```bash
# Open .env file and add your OpenRouter API key
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

Get a free API key from: https://openrouter.ai

### Step 4: Run the application
```bash
python run.py
```

You should see:
```
╔═══════════════════════════════════════════════════════╗
║   🤖 AI Research Agent Flask Application              ║
║   Starting server...                                  
║   🌐 Open: http://localhost:5000                      
║   📧 Login: admin / admin123                          
╚═══════════════════════════════════════════════════════╝
```

### Step 5: Open in browser
```
http://localhost:5000
```

**Login with:**
- Username: `admin`
- Password: `admin123`

---

## 🎯 Next: Important First Steps

### 1. Change Admin Password ⚠️ IMPORTANT
1. After login, go to Settings (top right)
2. Click "Change Password"
3. Enter current password: `admin123`
4. Enter new strong password
5. Click "Change Password"

### 2. Test a Query
1. Go to Dashboard (Home)
2. In the textarea, type: `"Explain how artificial intelligence works in simple terms"`
3. Click "Execute"
4. Wait 30-60 seconds for processing
5. View the result with reasoning process

### 3. Try Export
1. Once query completes, click "View"
2. Scroll down and click "📥 Export"
3. Choose format: TXT, PDF, or DOC
4. File downloads automatically

### 4. Check Admin Dashboard
1. Click "👑 Admin" in top navigation (appears if you're logged in as admin)
2. See system statistics
3. View all users and queries
4. Monitor task type breakdown

### 5. Create Test User
1. Go to login page (click Logout first)
2. Click "Register here"
3. Create a test account
4. Login with new account
5. Try executing a query as regular user

---

## 📂 Project Structure

```
research_agent_flask/
├── app.py                    ← Main application (start here to understand code)
├── run.py                    ← Easy launcher script
├── requirements.txt          ← All dependencies
├── .env                      ← Configuration (keep SECRET!)
├── README.md                 ← Full documentation
├── INSTALLATION.md           ← Detailed setup guide
│
├── templates/                ← HTML pages
│   ├── base.html            ← Navigation & styling
│   ├── login.html
│   ├── register.html
│   ├── index.html           ← Dashboard
│   ├── history.html         ← Query history
│   ├── query_detail.html    ← Query results & export
│   ├── settings.html
│   ├── error.html
│   └── admin/               ← Admin pages
│       ├── dashboard.html
│       ├── users.html
│       ├── queries.html
│       └── user_queries.html
│
└── research_agent.db        ← Database (auto-created)
```

---

## 🔐 Configuration

### .env File

**Location:** `research_agent_flask/.env`

**Key settings:**

```bash
# REQUIRED: Your OpenRouter API key
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Optional: Server settings
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Optional: For production, generate a new key:
# python -c "import os; print(os.urandom(24).hex())"
SECRET_KEY=your-generated-key
```

---

## 🌐 Access Points

### Local Machine
- **URL:** `http://localhost:5000`
- **Access from:** Same computer only

### Local Network
- **URL:** `http://your-computer-ip:5000`
- **Access from:** Other devices on same network
- **Note:** Change `FLASK_HOST=0.0.0.0` in .env (default)

### Deployed Online
- See INSTALLATION.md for cloud deployment options
- Recommended: Heroku, Railway, or Render

---

## 📚 Documentation

### Read in This Order

1. **QUICK_REFERENCE.md** ← Start here!
   - Quick commands
   - Feature overview
   - Troubleshooting

2. **README.md** (in project folder)
   - Complete documentation
   - All features explained
   - Configuration options

3. **INSTALLATION.md** (in project folder)
   - Detailed setup instructions
   - Common problems & solutions
   - Security setup

4. **COMPLETE_IMPLEMENTATION_SUMMARY.md** ← Detailed overview
   - What was built
   - Technical details
   - Architecture overview

---

## 🐛 Common Issues & Quick Fixes

### "Port 5000 already in use"
```bash
# Option 1: Use different port
# Edit .env and change:
FLASK_PORT=5001

# Option 2: Kill process on port 5000
lsof -ti:5000 | xargs kill -9  # macOS/Linux
```

### "ModuleNotFoundError: No module named 'flask'"
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or install specific package
pip install Flask==2.3.3
```

### "API Key Error"
```bash
# Check your API key:
1. Go to https://openrouter.ai/dashboard
2. Copy your key
3. Update .env file
4. Restart application
```

### "Database locked"
```bash
# Delete and recreate database
rm research_agent.db
python run.py
```

---

## ✨ Features Overview

### User Features
- ✅ Create account & login
- ✅ Execute AI research queries
- ✅ View reasoning process
- ✅ Export in multiple formats
- ✅ Query history with filtering
- ✅ Personal statistics
- ✅ Change password

### Admin Features
- ✅ View all users
- ✅ Monitor all queries
- ✅ System statistics
- ✅ Task type breakdown
- ✅ Query success rates
- ✅ User management

### Export Formats
- ✅ **TXT** - Plain text with all content
- ✅ **PDF** - Professional formatted document
- ✅ **DOC** - Microsoft Word format

---

## 🎨 Design

**Color Scheme:**
- Beige background (#DDD8CA)
- Lime green accent (#BEFF3F)
- Professional typography (Poppins)
- Responsive to all screen sizes
- Smooth animations and transitions

---

## 🔒 Security Notes

### Remember
- Default password is `admin123` - **Change this immediately!**
- Keep `.env` file secret
- Never commit `.env` to version control
- API key should never be in code

### For Production
- Use HTTPS
- Change SECRET_KEY
- Use strong passwords
- Set FLASK_DEBUG=False
- Regular database backups

---

## 📊 Default Admin Credentials

```
Username: admin
Password: admin123
```

**⚠️ CHANGE THIS FIRST!**

---

## 🚀 First Task: Execute a Query

1. Make sure app is running: `python run.py`
2. Open: http://localhost:5000
3. Login with admin/admin123
4. Go to Dashboard (should be default)
5. Click in the textarea
6. Type: `"Explain quantum computing"`
7. Click "Execute" button
8. Wait 30-60 seconds (with reasoning enabled)
9. Page will redirect to results automatically
10. Click "Show" under "🧠 AI Reasoning Process"
11. Scroll down to see AI's reasoning
12. Click "📥 Export" to download

---

## 💡 Pro Tips

1. **Longer responses:** Use words like "essay", "detailed", "comprehensive" in queries
2. **Faster processing:** Disable reasoning if needed (edit app.py)
3. **Multiple users:** Create test accounts to see multi-user features
4. **Admin features:** Login as admin to access admin dashboard
5. **Export formats:** Try all three export formats (TXT, PDF, DOC)
6. **Database:** The database is stored in `research_agent.db`
7. **Backups:** Regularly copy `research_agent.db` for backups

---

## 🎓 Learning Path

### Day 1: Setup
- [ ] Install dependencies
- [ ] Configure API key
- [ ] Run application
- [ ] Login with admin account

### Day 2: Core Features
- [ ] Change admin password
- [ ] Execute first query
- [ ] View reasoning process
- [ ] Export results

### Day 3: Exploration
- [ ] Create test user
- [ ] Try different query types
- [ ] Access admin dashboard
- [ ] View all queries as admin

### Day 4: Advanced
- [ ] Customize colors/fonts
- [ ] Add more users
- [ ] Monitor statistics
- [ ] Test all export formats

### Day 5: Deployment
- [ ] Consider cloud deployment
- [ ] Set up production environment
- [ ] Configure HTTPS
- [ ] Regular backups

---

## 📞 Help & Support

### For Issues:
1. **Check QUICK_REFERENCE.md** - Most answers are there!
2. **Read README.md** - Complete documentation
3. **Check INSTALLATION.md** - Setup problems
4. **Look in browser console** (F12) - Error messages
5. **Verify .env file** - Correct API key?

### Common Commands:
```bash
# Start application
python run.py

# Install missing package
pip install python-docx

# View all users
sqlite3 research_agent.db "SELECT * FROM user;"

# Stop server
Ctrl+C (in terminal)
```

---

## ✅ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] .env file updated with API key
- [ ] Application running (`python run.py`)
- [ ] Browser opened to http://localhost:5000
- [ ] Logged in successfully
- [ ] Password changed from default
- [ ] Executed test query
- [ ] Viewed reasoning process
- [ ] Exported result in at least one format
- [ ] Checked admin dashboard
- [ ] Created test user account

---

## 🎉 You're All Set!

Your AI Research Agent is ready to use!

**Start with:** `python run.py`

**Then open:** `http://localhost:5000`

**Login:** admin / admin123

**Remember:** Change the password on first login!

---

## 📞 Quick Reference

| Task | Steps |
|------|-------|
| Start app | `python run.py` |
| Stop app | `Ctrl+C` |
| Access | http://localhost:5000 |
| Default login | admin / admin123 |
| View docs | README.md |
| Setup help | INSTALLATION.md |
| Quick help | QUICK_REFERENCE.md |

---

## 🚀 Ready to Go!

Everything is configured and ready to use. Just follow these quick steps:

1. `cd research_agent_flask`
2. `pip install -r requirements.txt`
3. Update `OPENROUTER_API_KEY` in `.env`
4. `python run.py`
5. Open `http://localhost:5000`
6. Login & start researching!

**Enjoy your AI Research Agent! 🤖✨**
