from database import db
from openai_service import analyze_conversation
from models import Analysis
from datetime import datetime

async def process_sessions():
    await db.connect()
    sessions = await db.session.find_many()
    
    for session in sessions:
        messages = await db.message.find_many(where={"session_id": session.id})
        
        if messages:
            analysis = analyze_conversation(messages)
            if analysis:
                await db.analysis.create(
                    data={
                        "session_id": session.id,
                        "satisfaction": analysis["satisfaction"],
                        "summary": analysis["summary"],
                        "improvement": analysis["improvement"],
                        "created_at": datetime.utcnow(),
                    }
                )

    await db.disconnect()
