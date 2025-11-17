#!/usr/bin/env python
"""
Simple script to run the Flask application
"""
import os
from dotenv import load_dotenv
from app import app, init_db

if __name__ == '__main__':
    # Load environment variables
    load_dotenv()
    
    # Initialize database
    print("✅ Initializing database...")
    init_db()
    
    # Get configuration
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"""
    ╔═══════════════════════════════════════════════════════╗
    ║   🤖 AI Research Agent Flask Application              ║
    ║                                                       ║
    ║   Starting server...                                  ║
    ║   Host: {host}                                        
    ║   Port: {port}                                        
    ║   Debug: {debug}                                      
    ║                                                       ║
    ║   🌐 Open: http://localhost:{port}                    
    ║   📧 Login: admin / admin123                          
    ║                                                       ║
    ║   Press CTRL+C to stop                                ║
    ╚═══════════════════════════════════════════════════════╝
    """)
    
    # Run the application
    app.run(
        host=host,
        port=port,
        debug=debug
    )
