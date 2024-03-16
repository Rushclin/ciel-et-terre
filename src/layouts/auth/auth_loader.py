# auth/auth_loader.py

class AuthLoader:
    def authenticate(self, username: str, password: str):
        # Ajoutez la logique d'authentification ici
        # Retourne True si l'authentification réussit, False sinon

        if username == "admin@dsc.com" and password == "admin":
            return True
        return False
