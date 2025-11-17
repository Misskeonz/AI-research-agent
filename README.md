# 🤖 AI Research Agent - Flask Web Interface

A beautiful, feature-rich Flask web application for managing AI-powered research queries with SQLite database integration, user authentication, admin dashboard, and multi-format export capabilities.

## ✨ Features

✅ **User Authentication** - Secure login/registration system
✅ **AI Research Queries** - Execute research using OpenRouter API with advanced reasoning
✅ **Query Management** - View, organize, and manage research history
✅ **Reasoning Display** - Collapsible section showing AI's thinking process
✅ **Multi-Format Export** - Export results as TXT, PDF, or DOC
✅ **Admin Dashboard** - View all users and their research statistics
✅ **User Statistics** - Track query performance and task breakdowns
✅ **Responsive Design** - Beautiful UI with beige & lime green aesthetic
✅ **SQLite Database** - Persistent storage for users and queries
✅ **Background Processing** - Asynchronous query execution

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager
- OpenRouter API key

### Installation & Setup

#### Step 1: Install Dependencies

```bash
cd research_agent_flask
pip install -r requirements.txt
```

#### Step 2: Configure Environment

Edit `.env` file:

```bash
# Update your OpenRouter API key
OPENROUTER_API_KEY=your-key-here

# Change SECRET_KEY for production
SECRET_KEY=your-secure-key-here
```

#### Step 3: Initialize Database

```bash
# The database will auto-initialize on first run
# Default admin account will be created:
# Username: admin
# Password: admin123
```

#### Step 4: Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

---

## 📋 Default Login Credentials

After first run:
- **Username:** `admin`
- **Password:** `admin123`

⚠️ **IMPORTANT:** Change these credentials immediately in production!

---

## 📚 Project Structure

```
research_agent_flask/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .env                      # Environment configuration
├── templates/
│   ├── base.html            # Base template with navigation
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   ├── index.html           # Dashboard
│   ├── history.html         # Query history
│   ├── query_detail.html    # Query details with reasoning & export
│   ├── settings.html        # User settings
│   ├── error.html           # Error page
│   └── admin/
│       ├── dashboard.html   # Admin dashboard
│       ├── users.html       # User management
│       ├── queries.html     # All queries view
│       └── user_queries.html # User-specific queries
└── static/                  # CSS, JavaScript, images
```

---

## 🎨 Design Features

**Color Scheme:**
- Primary: Beige (#DDD8CA)
- Accent: Lime Green (#BEFF3F)
- Text: Dark Gray (#2a2a2a)

**Typography:**
- Primary: Poppins
- Accent: Playfair Display

**Components:**
- Modern card-based layout
- Smooth animations
- Responsive grid system
- Professional color scheme

---

## 🔐 User Management

### Create New User

1. Click "Register" on login page
2. Enter username and password (min 6 characters)
3. Confirm password
4. Account created! Login with credentials

### Admin Features

**Access Admin Dashboard:**
- Login with admin account
- Click "Admin Dashboard" in top navigation (admin only)

**Admin Capabilities:**
- View all users in system
- See total queries and statistics
- Track query success/failure rates
- View task type breakdown
- Monitor user-specific research history
- View recent queries across platform

### Change Password

- Go to Settings
- Click "Change Password"
- Enter current and new password
- Submit to update

---

## 🔍 Query Management

### Execute a Query

1. Go to Dashboard (home)
2. Enter your research query in textarea
3. Click "Execute" button
4. Query starts processing (shown in real-time)
5. When complete, view detailed results

### Query Details

For each query, view:
- **Query text** - Your original question
- **Response** - AI-generated answer
- **Reasoning** - Click "Show" to expand AI reasoning process
- **Tools Used** - Which tools were utilized
- **Execution Time** - How long it took
- **Task Type** - Automatically detected (code, analysis, creative, etc.)

### Export Results

Export any completed query in three formats:

**TXT Export:**
- Plain text format
- Includes query, response, reasoning, tools

**PDF Export:**
- Professional PDF document
- Formatted with headers and sections
- Includes all content

**DOC Export:**
- Microsoft Word format (.docx)
- Formatted text
- Easy editing

---

## 📊 Admin Dashboard

### Statistics Overview

Shows at-a-glance metrics:
- **Total Users** - All registered users
- **Total Queries** - All executed queries
- **Completed** - Successfully processed
- **Failed** - Errors or incomplete

### Task Type Breakdown

Visual breakdown of query types:
- Code
- Analysis
- Creative
- Research
- Problem Solving
- General

### Recent Queries

Latest 5 queries across all users with:
- User who submitted it
- Query preview
- Query type
- Current status
- Timestamp

### User Management

- View all users
- Sort by join date
- See query statistics per user
- Click to view user's complete query history

### All Queries View

Browse all queries from all users:
- User information
- Query preview
- Status
- Execution time
- Timestamp

---

## 🛠️ API Endpoints

### Public Routes

```
POST   /register              # User registration
POST   /login                 # User login
GET    /logout                # User logout
```

### Authenticated Routes

```
GET    /                      # Dashboard
GET    /history               # Query history
GET    /query/<id>            # Query details
GET    /settings              # User settings
```

### Admin Routes

```
GET    /admin                 # Admin dashboard
GET    /admin/users           # User management
GET    /admin/queries         # All queries
GET    /admin/user/<id>/queries  # User queries
```

### API Endpoints

```
POST   /api/execute-query     # Execute new query
GET    /api/query-status/<id> # Check query status
GET    /api/statistics        # Get user statistics
POST   /api/change-password   # Change password
```

### Export Endpoints

```
GET    /export/query/<id>/txt # Export as TXT
GET    /export/query/<id>/pdf # Export as PDF
GET    /export/query/<id>/doc # Export as DOC
```

---

## ⚙️ Configuration

### Adjust Max Tokens

Edit `app.py` in `execute_query_background()` function:

```python
# Change max_tokens parameter
max_tokens=8000,  # Increase for longer responses
```

### Change Model

```python
# In execute_query_background() function
model="openai/gpt-4-turbo",  # Use different model
```

### Database Location

```python
# In app.py configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///research_agent.db'
```

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Change port in .env
FLASK_PORT=5001

# Or kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

### Database Issues

```bash
# Remove old database
rm research_agent.db

# Restart app to recreate
python app.py
```

### API Key Error

- Verify OPENROUTER_API_KEY in .env
- Ensure API key is valid at https://openrouter.ai
- Check internet connection

### Queries Not Processing

- Check browser console for errors (F12)
- Verify OpenRouter API is working
- Check .env configuration

### Export Not Working

```bash
# Install required package for DOC export
pip install python-docx
```

---

## 📦 Deployment

### Production Setup

1. **Change Secret Key:**
   ```bash
   # Generate secure key
   python -c "import os; print(os.urandom(24).hex())"
   ```
   Update SECRET_KEY in .env

2. **Disable Debug Mode:**
   ```bash
   FLASK_DEBUG=False
   FLASK_ENV=production
   ```

3. **Use Production Server:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

4. **Use HTTPS:**
   - Configure SSL certificate
   - Use reverse proxy (Nginx/Apache)

5. **Database:**
   - Consider PostgreSQL for production
   - Update DATABASE_URL

### Heroku Deployment

1. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Deploy:
   ```bash
   heroku create your-app-name
   heroku config:set OPENROUTER_API_KEY=your-key
   git push heroku main
   ```

---

## 🔗 Important Links

- **OpenRouter**: https://openrouter.ai
- **OpenRouter Docs**: https://openrouter.ai/docs
- **Flask Docs**: https://flask.palletsprojects.com
- **SQLAlchemy Docs**: https://docs.sqlalchemy.org

---

## 📝 Environment Variables Reference

```bash
# Flask Configuration
SECRET_KEY              # Session encryption key
FLASK_ENV              # development or production
FLASK_DEBUG            # True or False
FLASK_HOST             # Server host (0.0.0.0)
FLASK_PORT             # Server port (5000)

# API Configuration
OPENROUTER_API_KEY     # Your OpenRouter API key

# Database
DATABASE_URL           # SQLite database path
SQLALCHEMY_TRACK_MODIFICATIONS  # False (recommended)
```

---

## 🎯 Feature Roadmap

Future enhancements:
- [ ] Team collaboration features
- [ ] Query scheduling
- [ ] Advanced analytics
- [ ] Query templates
- [ ] Integration with other APIs
- [ ] Email notifications
- [ ] Bulk query processing
- [ ] Query comparison tools

---

## 📄 License

This project is provided as-is for research and educational purposes.

---

## ✉️ Support

For issues or questions:
1. Check the Troubleshooting section
2. Review environment configuration
3. Check logs for error messages
4. Verify API connectivity

---

## 🎉 Getting Started Checklist

- [ ] Install Python 3.8+
- [ ] Clone/download project
- [ ] Run `pip install -r requirements.txt`
- [ ] Update .env with your API key
- [ ] Run `python app.py`
- [ ] Login with admin/admin123
- [ ] Change admin password
- [ ] Create test query
- [ ] Export result in multiple formats
- [ ] Check admin dashboard
- [ ] Create new user account

---

**Happy researching! 🚀**
