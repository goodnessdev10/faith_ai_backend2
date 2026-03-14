# Faith AI Backend

Faith AI Backend is the server-side system powering the Faith AI platform.

This backend handles:

- User authentication
- AI chat processing
- Subscription management
- Usage tracking
- Admin moderation tools
- Payment integration (Stripe / Paystack / Flutterwave)

## Project Structure

faith_ai_backend/
│
├── main.py
├── config/
├── models/
├── routes/
├── services/
├── schemas/

## Branch Strategy

main – stable production code  
dev – active development branch  

feature/authentication – login and registration  
feature/chat – AI chat endpoints  
feature/subscription – subscription system  

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- JWT Authentication
- AI API Integration

## Team Development

Developers should create feature branches from **dev** and submit pull requests after completing features.
