# 🛡️ Vault Guardian: Python Hashing System

I’ve been having a blast exploring Python Identity and Access Management! 

While looking for hands-on exercises, I came across 'The Vault Guardian'. It has been an incredible learning experience, and I wanted to share the key security concepts I've mastered through this project.

---

## 🧠 Technical Workflow

### 1. Cryptographic Library
The first step is to import `hashlib`, the Python library responsible for hashing and cryptography.

**Important:** Hashing is a one-way process; once content is hashed, it can **NEVER** be decrypted.

---

### 2. The Hashing Function
**The `generar_hash(password)`** function defines how the system processes raw text before storage.
* **`def`**: Used to define the function for generating the password hash.
* **`.encode()`**: Converts the password string into binary format.
* **`.sha256()`**: Acts as a "shredder," creating a non-human-readable object that Python can process.
* **`.hexdigest()`**: Transforms the internal object into a readable string of letters (a-f) and numbers (0-9).
* **`return`**: Instructs the system to save this information as `hash_resultante` for database storage.

---

### 3. Data Storage
The system utilizes an in-memory database that exists only while the program is running.
* It uses a dictionary structure: `base_de_datos = {}`.
* It starts empty and is populated during execution.

---

### 4. User Registration (`registrar_usuario`)
This function handles the creation of new credentials:
* It captures a username and password via `input`.
* The script `base_de_datos[usuario] = generar_hash(password)` is vital as it hashes the input and stores the result inside the user profile in the database.
* This ensures the username and password correspond and are saved in the same location.

---

### 5. Authentication Logic (`login`)
The login process uses an intuitive `if/else` flow to verify access:
* **Username Check**: It verifies if the `usuario_ingresado` exists in the database.
* **Hash Validation**: It generates a new hash for the entered password and compares it against the hash stored in the database.
* **Access Control**: 
    * If they match, it prints "Access granted".
    * If they do not match, it prints "Incorrect password" or "User does not exist".
 
---

### 6. Interactive Menu
A `while True` loop provides a continuous interface for the user:
* **Option 1**: Register a new user.
* **Option 2**: Log in.
* **Option 3**: View the database status (Usernames and Hashes).
* **Option 4**: Exit the system using the `break` command to end the loop.
* **Error Handling**: Any other input is marked as invalid.

---

## 🔒 Security Summary
By selecting Option 3, you can view the stored usernames and their corresponding hashes. Even with this visibility, the original passwords remain **completely unknown** and protected by the SHA-256 algorithm.

---

## 🚀 **My next step: putting it to the test in my virtual lab 💪**
