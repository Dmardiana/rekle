from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User


# Data users dari rekle_backup.sql (diurutkan berdasarkan ID)
USERS_FROM_BACKUP = [
    {
        "id": 1,
        "email": "admin@rekle.com",
        "full_name": "Admin Rekle",
        "phone_number": None,
        "hashed_password": "$2b$12$soKqODmaOADqvxJgog58m.FbUU1gAPHaiLDGkyhKRH.mnEe0965CC",
        "is_active": True,
        "is_superuser": True,
        "total_points": 0,
        "scan_count": 0,
        "action_count": 0,
        "avatar_url": None,
        "city": None,
        "bio": None,
        "balance": 0,
        "role": "user",
    },
    {
        "id": 2,
        "email": "user@rekle.com",
        "full_name": "User Rekle",
        "phone_number": None,
        "hashed_password": "$2b$12$CUJ5mb0xa4zsQpiyRvBpB.Vv43vVSnGw0uEQRzoBztjxjB92NcMva",
        "is_active": True,
        "is_superuser": False,
        "total_points": 0,
        "scan_count": 0,
        "action_count": 0,
        "avatar_url": None,
        "city": None,
        "bio": None,
        "balance": 0,
        "role": "user",
    },
]


def seed_users():
    db: Session = SessionLocal()

    try:
        for data in USERS_FROM_BACKUP:
            existing = db.query(User).filter(User.email == data["email"]).first()

            if not existing:
                user = User(
                    email=data["email"],
                    full_name=data["full_name"],
                    hashed_password=data["hashed_password"],  # hash asli dari backup
                    is_active=data["is_active"],
                    is_superuser=data["is_superuser"],
                    total_points=data["total_points"],
                    scan_count=data["scan_count"],
                    action_count=data["action_count"],
                    balance=data["balance"],
                )

                # Set field opsional jika ada di model
                for field in ("phone_number", "avatar_url", "city", "bio", "role"):
                    if hasattr(user, field):
                        setattr(user, field, data.get(field))

                db.add(user)
                print(f"✅ Created: {data['email']}")
            else:
                print(f"⏭️  Skipped (already exists): {data['email']}")

        db.commit()
        print("\n✅ Seeding selesai.")

    except Exception as e:
        db.rollback()
        print("❌ Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_users()