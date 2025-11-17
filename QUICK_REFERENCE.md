# ⚡ Quick Reference Guide

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API key in .env
OPENROUTER_API_KEY=your-key-here

# 3. Run application
python run.py

# 4. Open browser
http://localhost:5000

# 5. Login
Username: admin
Password: admin123
```

---

## 👤 User Types & Access

### Regular User
- Create account via registration
- Execute research queries
- View own query history
- Export results
- Change password
- View personal statistics

### Admin User
- Access admin dashboard
- View all users and their queries
- Monitor system statistics
- See task type breakdown
- Track query success rates

---

## 🎯 Main Features

### Execute Query
1. Go to Dashboard (Home)
2. Type research question in textarea
3. Click "Execute" button
4. Wait for processing (30-60 seconds with reasoning)
5. Click query to view results

### View Query Details
1. Go to History
2. Click "View" button on any query
3. See full query, response, reasoning
4. Scroll to reveal reasoning process
5. Export in any format

### Export Results
1. Open completed query
2. Click "📥 Export" button
3. Choose format:
   - 📄 TXT (plain text)
   - 📕 PDF (professional document)
   - 📗 DOC (Microsoft Word)
4. File automatically downloads

### View Query History
1. Go to History in navigation
2. See all your queries with status
3. Filter by task type or status
4. Click pagination for more queries
5. View details by clicking "View"

### Access Admin Dashboard
1. Login as admin (if applicable)
2. Click "👑 Admin" in top navigation
3. See system-wide statistics
4. View all users and queries
5. Monitor task type breakdown

---

## 🔑 Important Login Info

### Default Admin
```
URL:      http://localhost:5000
Username: admin
Password: admin123
```

**⚠️ Change this immediately after first login!**

---

## 🎨 Color Scheme

| Element | Color | Hex Code |
|---------|-------|----------|
| Primary Background | Beige | #DDD8CA |
| Accent | Lime Green | #BEFF3F |
| Text | Dark Gray | #2a2a2a |
| Cards | Light Beige | #F5F3ED |
| Borders | Tan | #E8E4D4 |

---

## 📂 File Locations

```
research_agent_flask/
├── app.py              # Main application
├── run.py              # Start here
├── .env                # Configuration
├── requirements.txt    # Dependencies
├── README.md           # Full documentation
├── INSTALLATION.md     # Setup guide
└── templates/          # HTML pages
    ├── base.html
    ├── login.html
    ├── index.html
    ├── history.html
    ├── query_detail.html
    └── admin/
```

---

## 🔧 Configuration (.env)

```bash
# API Key (REQUIRED)
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Server
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Security
SECRET_KEY=your-secret-key

# Environment
FLASK_ENV=development
FLASK_DEBUG=True
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 in use | Change FLASK_PORT in .env |
| Module not found | Run `pip install -r requirements.txt` |
| API error | Verify OPENROUTER_API_KEY in .env |
| Database locked | Delete `research_agent.db` and restart |
| Export not working | Run `pip install python-docx reportlab` |

---

## 📊 Admin Dashboard

### Metrics Shown
- Total users in system
- Total queries executed
- Completed queries
- Failed queries
- Task type breakdown
- Recent queries (last 5)

### Pages Available
- Dashboard - System overview
- Users - All registered users
- Queries - All queries system-wide
- User Queries - Specific user's queries

---

## 🔄 Task Types

Automatically detected from query text:

| Type | Keywords |
|------|----------|
| Code | python, javascript, function, algorithm |
| Analysis | analyze, analysis, explain, compare |
| Creative | write, story, poem, create, generate |
| Research | research, study, find, investigate |
| Problem Solving | solve, problem, fix, debug |
| General | other queries |

---

## 📈 Query Status Indicators

| Status | Meaning | Icon |
|--------|---------|------|
| Processing | Currently executing | ⏳ |
| Completed | Successfully processed | ✓ |
| Failed | Error occurred | ✗ |

---

## 🎯 Navigation Map

### User Navigation (All Users)
```
Home (Dashboard)
├── Execute Query
├── View Statistics
└── Quick Access to Recent Queries

History
├── View All Queries
├── Filter by Type/Status
└── Pagination

Settings
├── Change Password
├── View Personal Stats
└── Task Breakdown

Logout
```

### Admin Navigation (Admin Only)
```
Admin Dashboard (Additional)
├── View System Statistics
├── Monitor Recent Queries
└── Access Admin Pages

Admin Users
├── View All Users
├── See User Statistics
└── Go to User Queries

Admin Queries
├── View All Queries
├── See All Execution Times
└── Monitor Status

Admin User Queries
└── See Specific User's History
```

---

## 🛠️ API Endpoints Reference

### Authentication
```
POST   /register              Create account
POST   /login                 Login user
GET    /logout                Logout user
```

### Main Pages
```
GET    /                      Dashboard
GET    /history               Query history
GET    /query/<id>            Query details
GET    /settings              User settings
```

### Admin Pages
```
GET    /admin                 Admin dashboard
GET    /admin/users           User list
GET    /admin/queries         All queries
GET    /admin/user/<id>/queries  User queries
```

### API Calls
```
POST   /api/execute-query     Run query
GET    /api/query-status/<id> Check status
GET    /api/statistics        Get stats
POST   /api/change-password   Update password
```

### Export
```
GET    /export/query/<id>/txt Download as TXT
GET    /export/query/<id>/pdf Download as PDF
GET    /export/query/<id>/doc Download as DOC
```

---

## 💻 Common Commands

```bash
# Start application
python run.py

# Install dependencies
pip install -r requirements.txt

# Install missing package
pip install python-docx

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Generate secure key
python -c "import os; print(os.urandom(24).hex())"

# Test API key
curl -H "Authorization: Bearer YOUR_KEY" https://openrouter.ai/api/v1/auth/key/limits
```

---

## 🔐 Security Checklist

- [ ] Change admin password on first login
- [ ] Update SECRET_KEY for production
- [ ] Disable FLASK_DEBUG for production
- [ ] Use HTTPS in production
- [ ] Keep API key in .env (not in code)
- [ ] Regular database backups
- [ ] Monitor query execution logs
- [ ] Update dependencies regularly

---

## 📱 Browser Compatibility

| Browser | Support |
|---------|---------|
| Chrome | ✅ Full |
| Firefox | ✅ Full |
| Safari | ✅ Full |
| Edge | ✅ Full |
| IE 11 | ⚠️ Limited |

---

## ⏱️ Expected Performance

| Operation | Time |
|-----------|------|
| Query without reasoning | 5-10 seconds |
| Query with reasoning | 30-60 seconds |
| Page load | <1 second |
| Export to PDF | 2-5 seconds |
| Export to DOC | 1-3 seconds |

---

## 📞 Quick Help

**Can't login?**
- Username: admin
- Password: admin123
- URL: http://localhost:5000

**Query won't execute?**
- Check API key in .env
- Verify internet connection
- Check browser console (F12)

**Export not working?**
- Ensure query is completed (✓ status)
- Install: `pip install python-docx reportlab`
- Check browser permissions

**Port already in use?**
- Change FLASK_PORT in .env
- Or: `lsof -ti:5000 | xargs kill -9` (macOS/Linux)

---

## 📚 Documentation Files

Located in `research_agent_flask/`:

- **README.md** - Full documentation
- **INSTALLATION.md** - Setup instructions
- **app.py** - Source code with comments
- **This file** - Quick reference

---

## 🎓 Learning Path

1. **Day 1:** Install and run application
2. **Day 2:** Test query execution
3. **Day 3:** Explore admin dashboard
4. **Day 4:** Test export formats
5. **Day 5:** Create user accounts
6. **Day 6:** Customize colors/branding
7. **Day 7:** Deploy to cloud

---

## 🚀 Pro Tips

1. **Save queries offline** - Use Export feature
2. **Admin monitoring** - Check dashboard regularly
3. **Performance** - Start with simple queries first
4. **Backup database** - Copy `research_agent.db` regularly
5. **API limits** - Monitor OpenRouter usage
6. **Change passwords** - Security best practice
7. **Update dependencies** - Keep packages current

---

## 🎯 Feature Quick Access

| Feature | Location |
|---------|----------|
| Execute Query | Dashboard (Home page) |
| View History | History link in nav |
| Change Password | Settings page |
| Export Results | Query detail page |
| Admin Panel | Admin link (admin only) |
| View Statistics | Settings page |
| Reasoning | Query detail page (click "Show") |

---

## 💡 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| F12 | Open browser developer tools |
| Ctrl+L | Focus address bar |
| Ctrl+R | Refresh page |
| Ctrl+Shift+Delete | Clear cache |

---

## ✨ Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] API key in .env file
- [ ] Application running (`python run.py`)
- [ ] Browser open to `http://localhost:5000`
- [ ] Logged in with admin/admin123
- [ ] Password changed
- [ ] Test query executed
- [ ] Result exported
- [ ] Admin dashboard checked

---

## 📞 Support

1. Check README.md for detailed documentation
2. Check INSTALLATION.md for setup issues
3. Review browser console for errors (F12)
4. Verify .env configuration
5. Ensure API key is valid

---

**Happy researching! 🚀**

For more details, see the full documentation in README.md and INSTALLATION.md
