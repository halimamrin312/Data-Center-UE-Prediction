# 🚀 Panduan Setup GitHub Repository

## 📋 Checklist Sebelum Push

### ✅ File yang Sudah Siap:

- [x] `README.md` - Dokumentasi lengkap project
- [x] `requirements.txt` - Python dependencies
- [x] `.gitignore` - File yang tidak perlu di-commit
- [x] `LICENSE` - MIT License
- [x] `CONTRIBUTING.md` - Guidelines untuk kontributor
- [x] `CHANGELOG.md` - Version history
- [x] `predict.py` - Script prediksi production-ready
- [x] `main.ipynb` - Notebook lengkap (EDA → Modeling → Deployment)
- [x] `asisten.md` - Panduan asisten
- [x] `data_center_hybrid.csv` - Dataset

### ⚠️ File yang TIDAK Perlu di-Push:

- `.venv/` - Virtual environment (sudah ada di .gitignore)
- `models/*.joblib` - Model files terlalu besar (sudah ada di .gitignore)
- `.ipynb_checkpoints/` - Jupyter checkpoints (sudah ada di .gitignore)

---

## 🔧 Langkah-Langkah Push ke GitHub

### 1. Inisialisasi Git Repository

```bash
cd /home/tdr-5000/Documents/AiDataCenter
git init
```

### 2. Konfigurasi Git (jika belum)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Add Files ke Staging

```bash
# Add semua file (kecuali yang ada di .gitignore)
git add .

# atau add file spesifik:
git add README.md requirements.txt .gitignore LICENSE
git add main.ipynb predict.py CONTRIBUTING.md CHANGELOG.md
git add data_center_hybrid.csv asisten.md
```

### 4. Commit Changes

```bash
git commit -m "Initial commit: Data Center PUE Prediction ML Project

- Complete EDA with visualizations
- Data preprocessing pipeline
- Multiple ML models (Linear Regression, Random Forest, Gradient Boosting)
- Best model: Random Forest (R² = 0.8057)
- Model deployment with joblib
- Production-ready prediction script
- Complete documentation"
```

### 5. Buat Repository di GitHub

1. Buka https://github.com
2. Click **"+"** → **"New repository"**
3. Isi:
   - **Repository name**: `AiDataCenter` (atau nama lain)
   - **Description**: "Machine Learning project untuk prediksi PUE Data Center"
   - **Public** atau **Private**
   - **JANGAN** check "Add a README file" (karena sudah ada)
4. Click **"Create repository"**

### 6. Link ke Remote Repository

```bash
# Replace YOUR_USERNAME dengan username GitHub Anda
git remote add origin https://github.com/YOUR_USERNAME/AiDataCenter.git

# Atau jika pakai SSH:
git remote add origin git@github.com:YOUR_USERNAME/AiDataCenter.git
```

### 7. Push ke GitHub

```bash
# Push branch main
git branch -M main
git push -u origin main
```

---

## 🎯 Setelah Push

### 1. Update README.md di GitHub

Edit bagian ini di README.md:

```markdown
## 👤 Author

**Your Name**
- GitHub: [@your_username](https://github.com/your_username)
- LinkedIn: [Your Name](https://linkedin.com/in/your_profile)
```

Ganti dengan informasi Anda yang sebenarnya.

### 2. Tambah GitHub Topics/Tags

Di halaman repository GitHub:
1. Click **"⚙️ Settings"**
2. Di bagian **"Topics"**, tambahkan:
   - `machine-learning`
   - `data-science`
   - `python`
   - `scikit-learn`
   - `random-forest`
   - `data-center`
   - `pue`
   - `jupyter-notebook`

### 3. Setup GitHub Pages (Optional)

Jika ingin dokumentasi online:
1. Settings → Pages
2. Source: Deploy from branch `main`
3. Select folder: `/(root)`

---

## 📦 Mengelola Model Files

### Opsi 1: Git LFS (Large File Storage)

Jika ingin commit model files:

```bash
# Install Git LFS
git lfs install

# Track model files
git lfs track "models/*.joblib"
git add .gitattributes
git commit -m "Setup Git LFS for model files"
git push
```

### Opsi 2: Cloud Storage (Recommended)

Upload model files ke:
- **Google Drive**
- **Dropbox**
- **AWS S3**
- **Hugging Face Hub**

Tambahkan link download di README.md.

### Opsi 3: Releases

Upload model files sebagai release assets:

1. GitHub → Releases → **"Create a new release"**
2. Tag version: `v1.0.0`
3. Upload model files sebagai assets
4. Publish release

---

## 🔄 Update Repository Nanti

### Jika Ada Perubahan:

```bash
# Check status
git status

# Add changes
git add .

# Commit
git commit -m "Descriptive commit message"

# Push
git push origin main
```

---

## ❓ Troubleshooting

### Error: "fatal: remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/AiDataCenter.git
```

### Error: "Permission denied (publickey)"

Gunakan HTTPS atau setup SSH key:
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
# Follow instructions
# Add SSH key ke GitHub Settings
```

### File Terlalu Besar

Jika ada error "file too large":
1. Check `.gitignore` sudah benar
2. Gunakan Git LFS
3. Atau remove file dari staging:
   ```bash
   git rm --cached path/to/large/file
   ```

---

## ✨ Tips

1. **Commit Often**: Commit kecil dan sering lebih baik dari commit besar
2. **Descriptive Messages**: Write clear commit messages
3. **Branch Strategy**: Gunakan branches untuk features baru
4. **Documentation**: Update README.md setiap ada perubahan signifikan
5. **Tags/Releases**: Gunakan semantic versioning (v1.0.0, v1.1.0, dll)

---

## 📚 Resources

- [GitHub Docs](https://docs.github.com)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Git LFS](https://git-lfs.github.com/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)

---

**Good luck with your project! 🚀**
