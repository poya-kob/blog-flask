from app_bone import create_app
import app_bone

if __name__ == "__main__":
    app = create_app(celery=app_bone.celery)
    app.run(debug=True)
