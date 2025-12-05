# 🤖 Assistant IA Low-Cost - Nuit de l'Info 2025

Assistant intelligent léger pour accès aux services publics numériques, optimisé pour les **connexions faibles ou instables**. 

[![PWA](https://img.shields.io/badge/PWA-Ready-success)](https://developer.mozilla.org/fr/docs/Web/Progressive_web_apps)
[![i18n](https://img.shields.io/badge/i18n-FR%20%7C%20AR-blue)](https://www.i18next.com/)
[![Offline](https://img.shields.io/badge/Offline-Capable-orange)](https://developer.mozilla.org/fr/docs/Web/API/Service_Worker_API)

## ✨ Fonctionnalités

### 🚦 3 Modes Adaptatifs
- **🔴 Offline** - Recherche par mots-clés dans IndexedDB (< 200ms)
- **🟡 Hybride** - RAG avec embeddings locaux (< 3s)
- **🟢 Online** - API backend complète (< 1s)

Le mode s'adapte **automatiquement** selon la qualité de connexion détectée.

### 🌍 Support Multilingue
- **Français** (par défaut)
- **العربية** avec layout RTL automatique

### 📱 Progressive Web App
- ✅ Installation sur mobile/desktop
- ✅ Fonctionnement offline partiel
- ✅ Service Worker intelligent
- ✅ Caching stratégique

### 🧠 IA Légère
- Embeddings multilingues (MiniLM-L12-v2)
- RAG (Retrieval-Augmented Generation)
- Recherche sémantique locale
- Fallback automatique

## 🚀 Installation

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

L'application sera disponible sur [http://localhost:3000](http://localhost:3000)

### Data Collection (Python)

```bash
cd data-collection
pip install -r requirements.txt

# Scraper le site nuitdelinfo.com
python 01_scraper_advanced.py

# Nettoyer et structurer
python 03_data_cleaner.py

# Générer embeddings
python 05_embeddings_creator.py
```

Ou utilisez le script automatique:
```bash
cd data-collection
./update_data.sh
```

## 📂 Structure du Projet

```
assistant-ia-nuit-info/
├── frontend/                    # Application React
│   ├── public/
│   │   ├── data/
│   │   │   ├── faqs.json       # Base de données FAQ
│   │   │   └── embeddings.json # Vecteurs sémantiques
│   │   ├── service-worker.js   # PWA offline
│   │   └── manifest.json       # Configuration PWA
│   └── src/
│       ├── components/         # Composants React
│       │   ├── Chat/           # Interface chat
│       │   └── UI/             # Composants UI
│       ├── services/
│       │   ├── aiEngine/       # 3 moteurs IA
│       │   ├── storage/        # IndexedDB
│       │   ├── ml/             # RAG, embeddings
│       │   └── api/            # Backend API
│       ├── hooks/              # useChat, useConnection
│       ├── locales/            # i18n FR/AR
│       └── styles/             # CSS avec RTL
│
├── data-collection/            # Scripts Python
│   ├── 01_scraper_advanced.py # Web scraping
│   ├── 03_data_cleaner.py     # Nettoyage données
│   ├── 05_embeddings_creator.py # Génération embeddings
│   └── requirements.txt        # Dépendances Python
│
├── description.txt             # Cahier des charges
└── documentation.txt           # Documentation complète
```

## 🎯 Utilisation

### Développement

```bash
# Frontend
cd frontend
npm start

# Tests E2E
npm test

# Build production
npm run build
```

### Mise à Jour des Données

Les données du site [nuitdelinfo.com](https://www.nuitdelinfo.com/) peuvent changer. Pour mettre à jour:

```bash
cd data-collection
./update_data.sh
```

## 🌐 Déploiement

### Vercel (Recommandé)

```bash
npm install -g vercel
cd frontend
vercel
```

Configuration incluse dans `vercel.json`.

### Autres hébergeurs

Build puis déployez le dossier `frontend/build/`:
```bash
cd frontend
npm run build
```

Compatible avec:
- Netlify
- GitHub Pages
- Firebase Hosting
- AWS S3 + CloudFront

## 🛠️ Technologies

### Frontend
- **React 18** - Framework UI
- **i18next** - Internationalisation FR/AR
- **idb** - IndexedDB wrapper
- **Service Workers** - PWA offline

### Data Collection
- **Selenium** - Web scraping dynamique
- **BeautifulSoup4** - Parsing HTML
- **sentence-transformers** - Embeddings ML
- **pandas** - Traitement données

### IA/ML
- **RAG** - Retrieval-Augmented Generation
- **Cosine Similarity** - Recherche sémantique
- **MiniLM-L12-v2** - Modèle multilingue (384d)

## 📊 Performance

| Mode | Temps réponse | Précision | Connexion requise |
|------|---------------|-----------|-------------------|
| Offline | < 200ms | ~60% | ❌ Non |
| Hybride | < 3s | ~80% | 🟡 Faible |
| Online | < 1s | ~95% | ✅ Oui |

## 🔒 Sécurité

- Headers sécurisés (CSP, X-Frame-Options)
- Pas de stockage de données sensibles
- Validation côté client
- HTTPS recommandé en production

## 📝 License

Projet réalisé dans le cadre de la **Nuit de l'Info 2025** - FST Nouakchott

## 🤝 Contribution

Pour améliorer le projet:
1. Fork le repository
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit (`git commit -m 'Ajout fonctionnalité'`)
4. Push (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📞 Support

Pour toute question sur le projet ou la Nuit de l'Info:
- Site officiel: [www.nuitdelinfo.com](https://www.nuitdelinfo.com/)
- Documentation: `documentation.txt`

---

**Fait avec ❤️ pour la Nuit de l'Info 2025**
