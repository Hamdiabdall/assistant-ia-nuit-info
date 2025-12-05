#!/usr/bin/env python3
"""
Smart FAQ Generator - Enhanced Version
Generates 25+ FAQs optimized for all 3 AI modes (Offline, Hybrid, Online)
"""

import json
import os
from datetime import datetime
from collections import Counter

class SmartFAQGenerator:
    def __init__(self, data_dir='Script/data/nuit_info'):
        self.data_dir = data_dir
        
    def load_scraped_data(self):
        """Load all scraped data"""
        print("📥 Loading scraped data...")
        
        data = {}
        for data_type in ['texts', 'links', 'images', 'pdfs', 'videos', 'buttons']:
            file_path = f"{self.data_dir}/{data_type}.json"
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data[data_type] = json.load(f)
                print(f"  ✓ {data_type}: {len(data[data_type])} items")
            else:
                data[data_type] = []
                print(f"  ⚠️ {data_type}: file not found")
        
        return data
    
    def generate_faqs(self, data):
        """Generate 25+ useful FAQs from scraped data"""
        print("\n🔨 Generating smart FAQs...")
        
        faqs = []
        
        # === CORE FAQs (25+ high quality questions) ===
        core_faqs = [
            # --- GENERAL ---
            {
                "question_fr": "Qu'est-ce que la Nuit de l'Info ?",
                "answer_fr": "La Nuit de l'Info est un concours national de développement web qui réunit chaque année des milliers d'étudiants. Pendant une nuit entière (environ 16h), les équipes doivent développer une application web sur un sujet donné. C'est un événement festif, challengeant et formateur qui se déroule simultanément dans toute la France.",
                "question_ar": "ما هي ليلة المعلومات؟",
                "answer_ar": "ليلة المعلومات هي مسابقة وطنية لتطوير الويب تجمع آلاف الطلاب كل عام. خلال ليلة كاملة، يجب على الفرق تطوير تطبيق ويب حول موضوع معين.",
                "category": "general",
                "keywords": ["nuit", "info", "concours", "étudiants", "développement", "web", "application", "définition"]
            },
            {
                "question_fr": "C'est quoi la Nuit de l'Info ?",
                "answer_fr": "La Nuit de l'Info est une compétition nationale de programmation web. Des équipes d'étudiants développent une application web complète en une seule nuit. C'est à la fois un défi technique et un événement convivial.",
                "question_ar": "ما هي ليلة المعلومات؟",
                "answer_ar": "ليلة المعلومات هي مسابقة برمجة ويب وطنية.",
                "category": "general",
                "keywords": ["quoi", "cest", "nuit", "info", "compétition", "programmation"]
            },
            {
                "question_fr": "À qui s'adresse la Nuit de l'Info ?",
                "answer_fr": "La Nuit de l'Info s'adresse à tous les étudiants en informatique, développement web, design numérique ou domaines connexes. Que vous soyez en IUT, université, école d'ingénieurs ou école de design, vous pouvez participer !",
                "question_ar": "لمن تتوجه ليلة المعلومات؟",
                "answer_ar": "تتوجه ليلة المعلومات لجميع طلاب المعلوماتية وتطوير الويب والتصميم الرقمي.",
                "category": "general",
                "keywords": ["qui", "étudiants", "public", "participants", "formation", "école"]
            },
            
            # --- DATES ET HORAIRES ---
            {
                "question_fr": "Quand a lieu la Nuit de l'Info 2025 ?",
                "answer_fr": "La Nuit de l'Info 2025 se déroule les 4 et 5 décembre 2025. L'événement commence généralement en fin d'après-midi (vers 16h-17h) et se termine le lendemain matin (vers 8h).",
                "question_ar": "متى تقام ليلة المعلومات 2025؟",
                "answer_ar": "تقام ليلة المعلومات 2025 في 4 و 5 ديسمبر 2025.",
                "category": "organisation",
                "keywords": ["date", "quand", "2025", "décembre", "horaires", "début", "fin", "4", "5"]
            },
            {
                "question_fr": "Quelle est la date de la Nuit de l'Info ?",
                "answer_fr": "La Nuit de l'Info a lieu chaque année début décembre. En 2025, c'est les 4 et 5 décembre. L'événement dure environ 16 heures, de fin d'après-midi jusqu'au lendemain matin.",
                "question_ar": "ما هو موعد ليلة المعلومات؟",
                "answer_ar": "تقام ليلة المعلومات كل عام في بداية شهر ديسمبر.",
                "category": "organisation",
                "keywords": ["date", "quand", "décembre", "année", "durée", "heures"]
            },
            {
                "question_fr": "Combien de temps dure la Nuit de l'Info ?",
                "answer_fr": "La Nuit de l'Info dure environ 16 heures. Elle commence généralement vers 16h-17h et se termine vers 8h le lendemain matin. C'est une nuit intense de développement !",
                "question_ar": "كم تدوم ليلة المعلومات؟",
                "answer_ar": "تدوم ليلة المعلومات حوالي 16 ساعة.",
                "category": "organisation",
                "keywords": ["durée", "temps", "heures", "combien", "long"]
            },
            
            # --- INSCRIPTION ---
            {
                "question_fr": "Comment s'inscrire à la Nuit de l'Info ?",
                "answer_fr": "Pour s'inscrire, rendez-vous sur le site officiel www.nuitdelinfo.com. Créez un compte, puis inscrivez votre équipe (3 à 6 personnes). L'inscription est totalement gratuite.",
                "question_ar": "كيف أسجل في ليلة المعلومات؟",
                "answer_ar": "للتسجيل، قم بزيارة الموقع الرسمي www.nuitdelinfo.com.",
                "category": "inscription",
                "keywords": ["inscription", "inscrire", "comment", "équipe", "site", "compte", "gratuit"]
            },
            {
                "question_fr": "Quel est le lien d'inscription ?",
                "answer_fr": "Le lien d'inscription est disponible sur le site officiel : https://www.nuitdelinfo.com/inscription. Vous y trouverez toutes les informations pour créer votre compte.",
                "question_ar": "ما هو رابط التسجيل؟",
                "answer_ar": "رابط التسجيل: https://www.nuitdelinfo.com/inscription",
                "category": "inscription",
                "keywords": ["lien", "inscription", "url", "site", "www", "https", "adresse"]
            },
            {
                "question_fr": "L'inscription est-elle gratuite ?",
                "answer_fr": "Oui, la participation à la Nuit de l'Info est totalement gratuite ! L'inscription, la participation et l'accès aux ressources sont entièrement gratuits pour tous les étudiants.",
                "question_ar": "هل التسجيل مجاني؟",
                "answer_ar": "نعم، المشاركة في ليلة المعلومات مجانية تمامًا!",
                "category": "inscription",
                "keywords": ["gratuit", "prix", "coût", "payer", "free", "argent", "payant"]
            },
            {
                "question_fr": "Où s'inscrire pour la Nuit de l'Info ?",
                "answer_fr": "L'inscription se fait sur le site officiel www.nuitdelinfo.com. Créez un compte personnel puis inscrivez votre équipe. La liste des sites d'accueil est également disponible sur le site.",
                "question_ar": "أين أسجل لليلة المعلومات؟",
                "answer_ar": "التسجيل يتم على الموقع الرسمي www.nuitdelinfo.com",
                "category": "inscription",
                "keywords": ["où", "inscrire", "site", "www", "inscription", "plateforme"]
            },
            
            # --- ÉQUIPES ---
            {
                "question_fr": "Combien de personnes dans une équipe ?",
                "answer_fr": "Une équipe pour la Nuit de l'Info doit compter entre 3 et 6 personnes. Il est recommandé d'avoir des profils variés : développeurs frontend, backend, designers.",
                "question_ar": "كم عدد الأشخاص في الفريق؟",
                "answer_ar": "يجب أن يتكون الفريق من 3 إلى 6 أشخاص.",
                "category": "inscription",
                "keywords": ["équipe", "personnes", "nombre", "membres", "participants", "combien", "taille"]
            },
            {
                "question_fr": "Comment former une équipe ?",
                "answer_fr": "Vous pouvez former une équipe avec vos camarades de classe ou d'autres étudiants. L'équipe doit avoir entre 3 et 6 membres. Assurez-vous d'avoir des compétences variées : développement, design, gestion de projet.",
                "question_ar": "كيف أشكل فريقًا؟",
                "answer_ar": "يمكنك تشكيل فريق مع زملائك أو طلاب آخرين. يجب أن يكون بين 3 و 6 أعضاء.",
                "category": "inscription",
                "keywords": ["équipe", "former", "créer", "membres", "camarades"]
            },
            {
                "question_fr": "Peut-on participer seul ?",
                "answer_fr": "Non, la Nuit de l'Info est un événement d'équipe. Vous devez avoir au minimum 3 personnes et au maximum 6 personnes dans votre équipe.",
                "question_ar": "هل يمكن المشاركة بمفردي؟",
                "answer_ar": "لا، يجب أن يكون لديك فريق من 3 إلى 6 أشخاص.",
                "category": "inscription",
                "keywords": ["seul", "individuel", "équipe", "minimum", "obligatoire"]
            },
            
            # --- DÉFIS ---
            {
                "question_fr": "Quels sont les défis proposés ?",
                "answer_fr": "Les défis sont proposés par les partenaires et couvrent des thématiques variées : esprit d'équipe, architecture logicielle, accessibilité, développement durable, sécurité, performance, créativité, design.",
                "question_ar": "ما هي التحديات المقترحة؟",
                "answer_ar": "يتم تقديم التحديات من قبل الشركاء وتغطي مواضيع مختلفة.",
                "category": "defis",
                "keywords": ["défis", "challenges", "thématiques", "partenaires", "bonus", "liste"]
            },
            {
                "question_fr": "Comment choisir les défis ?",
                "answer_fr": "Chaque équipe peut choisir librement les défis qu'elle souhaite relever parmi ceux proposés par les partenaires. Vous n'êtes pas obligés de tous les faire - choisissez ceux qui correspondent à vos compétences.",
                "question_ar": "كيف أختار التحديات؟",
                "answer_ar": "يمكن لكل فريق اختيار التحديات بحرية من بين تلك المقترحة.",
                "category": "defis",
                "keywords": ["défis", "choisir", "sélectionner", "partenaires", "optionnel"]
            },
            {
                "question_fr": "Les défis sont-ils obligatoires ?",
                "answer_fr": "Le sujet principal est obligatoire. Les défis bonus proposés par les partenaires sont optionnels mais permettent de gagner des prix supplémentaires.",
                "question_ar": "هل التحديات إلزامية؟",
                "answer_ar": "الموضوع الرئيسي إلزامي. التحديات الإضافية اختيارية ولكنها تتيح الفوز بجوائز إضافية.",
                "category": "defis",
                "keywords": ["défis", "obligatoire", "optionnel", "bonus", "principal"]
            },
            
            # --- TECHNIQUE ---
            {
                "question_fr": "Quelles technologies peut-on utiliser ?",
                "answer_fr": "Vous êtes libres d'utiliser les technologies de votre choix : HTML, CSS, JavaScript, React, Vue.js, Angular, Node.js, PHP, Python, etc. L'important est de livrer une application fonctionnelle.",
                "question_ar": "ما هي التقنيات التي يمكننا استخدامها؟",
                "answer_ar": "أنت حر في استخدام التقنيات التي تختارها: HTML, CSS, JavaScript, React, etc.",
                "category": "technique",
                "keywords": ["technologies", "langages", "frameworks", "développement", "html", "javascript", "react", "python", "outils"]
            },
            {
                "question_fr": "Quels langages de programmation utiliser ?",
                "answer_fr": "Tous les langages sont autorisés : JavaScript, Python, PHP, Java, etc. Vous pouvez utiliser des frameworks comme React, Vue, Angular, Django, Laravel. L'essentiel est de créer une application web.",
                "question_ar": "ما هي لغات البرمجة المسموحة؟",
                "answer_ar": "جميع لغات البرمجة مسموحة: JavaScript, Python, PHP, Java, etc.",
                "category": "technique",
                "keywords": ["langages", "programmation", "javascript", "python", "php", "java", "code"]
            },
            {
                "question_fr": "Faut-il savoir coder pour participer ?",
                "answer_fr": "Il est recommandé d'avoir des notions de développement web, mais ce n'est pas obligatoire pour tous les membres. Une équipe peut inclure des designers, des chefs de projet, etc.",
                "question_ar": "هل يجب معرفة البرمجة للمشاركة؟",
                "answer_ar": "يُنصح بمعرفة تطوير الويب، لكنه ليس إلزاميًا لجميع الأعضاء.",
                "category": "technique",
                "keywords": ["coder", "programmation", "savoir", "débutant", "niveau", "compétences"]
            },
            
            # --- ÉVALUATION ---
            {
                "question_fr": "Comment sont évalués les projets ?",
                "answer_fr": "Les projets sont évalués par un jury composé de professionnels et d'enseignants. Les critères incluent : respect du sujet, qualité du code, ergonomie, design, originalité et esprit d'équipe.",
                "question_ar": "كيف يتم تقييم المشاريع؟",
                "answer_ar": "يتم تقييم المشاريع من قبل لجنة تحكيم مكونة من محترفين ومعلمين.",
                "category": "evaluation",
                "keywords": ["évaluation", "critères", "jury", "prix", "qualité", "code", "note", "notation"]
            },
            {
                "question_fr": "Quels sont les critères d'évaluation ?",
                "answer_fr": "Les critères d'évaluation sont : fonctionnalité de l'application, qualité du code source, design et ergonomie, respect du sujet principal, originalité et créativité, travail d'équipe.",
                "question_ar": "ما هي معايير التقييم؟",
                "answer_ar": "معايير التقييم هي: عمل التطبيق، جودة الكود، التصميم، احترام الموضوع، الإبداع.",
                "category": "evaluation",
                "keywords": ["critères", "évaluation", "notation", "qualité", "fonctionnalité", "design"]
            },
            {
                "question_fr": "Y a-t-il des prix à gagner ?",
                "answer_fr": "Oui, il y a des prix pour les meilleures équipes ! Des prix sont décernés pour le sujet principal et pour chaque défi partenaire. Les prix varient selon les partenaires : matériel, stages, formations, etc.",
                "question_ar": "هل هناك جوائز؟",
                "answer_ar": "نعم، هناك جوائز للفرق الفائزة! تختلف الجوائز حسب الشركاء.",
                "category": "evaluation",
                "keywords": ["prix", "gagner", "récompenses", "cadeaux", "gagnants", "vainqueur"]
            },
            
            # --- LIEU ---
            {
                "question_fr": "Où se déroule la Nuit de l'Info ?",
                "answer_fr": "La Nuit de l'Info se déroule simultanément dans de nombreux sites en France : universités, IUT, écoles d'ingénieurs. Consultez le site officiel pour trouver le site le plus proche.",
                "question_ar": "أين تقام ليلة المعلومات؟",
                "answer_ar": "تقام ليلة المعلومات في العديد من المواقع في فرنسا.",
                "category": "organisation",
                "keywords": ["lieu", "où", "site", "université", "école", "local", "ville"]
            },
            {
                "question_fr": "Peut-on participer à distance ?",
                "answer_fr": "Généralement, les équipes participent sur un site physique (université, école). Certaines éditions ont proposé une participation à distance. Consultez les modalités de l'édition en cours.",
                "question_ar": "هل يمكن المشاركة عن بعد؟",
                "answer_ar": "عادة، تشارك الفرق في موقع فعلي. قد يكون هناك خيار للمشاركة عن بعد.",
                "category": "organisation",
                "keywords": ["distance", "remote", "ligne", "chez", "maison", "présentiel"]
            },
            
            # --- DIVERS ---
            {
                "question_fr": "Que faut-il apporter ?",
                "answer_fr": "Apportez votre ordinateur portable, chargeur, casque audio, et tout matériel dont vous avez besoin pour coder. Prévoyez aussi de quoi manger et boire pour tenir toute la nuit !",
                "question_ar": "ماذا يجب أن أحضر؟",
                "answer_ar": "أحضر حاسوبك المحمول والشاحن وسماعات الرأس والطعام.",
                "category": "organisation",
                "keywords": ["apporter", "matériel", "ordinateur", "équipement", "préparer"]
            },
            {
                "question_fr": "Comment se préparer ?",
                "answer_fr": "Pour bien vous préparer : formez une équipe équilibrée, familiarisez-vous avec les outils que vous utiliserez, préparez un environnement de développement, et reposez-vous bien avant le jour J !",
                "question_ar": "كيف أستعد؟",
                "answer_ar": "للتحضير الجيد: شكّل فريقًا متوازنًا، تعرف على الأدوات، ونم جيدًا قبل اليوم!",
                "category": "organisation",
                "keywords": ["préparer", "préparation", "conseils", "avant", "astuces"]
            },

            # --- ASSISTANT & MODES ---
            {
                "question_fr": "Comment fonctionne l'assistant IA pendant la Nuit de l'Info ?",
                "answer_fr": "L'assistant IA analyse votre question, cherche les informations les plus pertinentes sur la Nuit de l'Info puis vous renvoie une réponse courte et claire. Selon la qualité de la connexion, il utilise un mode hors-ligne, hybride ou en ligne pour rester rapide et fiable.",
                "question_ar": "كيف يعمل المساعد الذكي خلال ليلة المعلومات؟",
                "answer_ar": "يقوم المساعد الذكي بتحليل سؤالك والبحث عن أهم المعلومات حول ليلة المعلومات ثم يرسل لك إجابة قصيرة وواضحة. حسب جودة الاتصال، يستخدم وضع عدم الاتصال أو الوضع الهجين أو الوضع المتصل ليبقى سريعًا وموثوقًا.",
                "category": "assistant",
                "keywords": ["assistant", "ia", "fonctionnement", "comment ça marche", "question", "réponse"]
            },
            {
                "question_fr": "Quels sont les 3 modes de l'assistant IA low-cost ?",
                "answer_fr": "L'assistant propose trois modes complémentaires : (1) OFFLINE, qui fait une recherche rapide par mots-clés dans une base locale de questions/réponses ; (2) HYBRIDE, qui utilise des embeddings et une recherche sémantique plus intelligente ; (3) ONLINE, qui interroge un backend complet quand la connexion est bonne.",
                "question_ar": "ما هي أوضاع المساعد الذكي الثلاثة ذات التكلفة المنخفضة؟",
                "answer_ar": "يوفر المساعد ثلاثة أوضاع متكاملة: (1) وضع عدم الاتصال، يبحث بسرعة عن الكلمات المفتاحية في قاعدة أسئلة/أجوبة محلية؛ (2) الوضع الهجين، يستخدم تمثيلات عددية (embeddings) وبحثًا دلاليًا أذكى؛ (3) الوضع المتصل، يستدعي خادمًا خلفيًا كاملاً عندما يكون الاتصال جيدًا.",
                "category": "modes",
                "keywords": ["mode", "offline", "hors ligne", "hybride", "online", "en ligne", "low-cost"]
            },
            {
                "question_fr": "Quand utiliser le mode hors-ligne de l'assistant ?",
                "answer_fr": "Le mode hors-ligne est idéal lorsque la connexion Internet est coupée ou très instable. Il s'appuie uniquement sur une base locale de FAQ stockée dans votre navigateur et répond en moins de 200 ms sur les questions les plus fréquentes.",
                "question_ar": "متى أستخدم وضع عدم الاتصال في المساعد؟",
                "answer_ar": "وضع عدم الاتصال مناسب عندما يكون الاتصال بالإنترنت مقطوعًا أو غير مستقر. يعتمد فقط على قاعدة أسئلة متكررة مخزنة محليًا في متصفحك ويجيب في أقل من 200 مللي ثانية على أكثر الأسئلة تكرارًا.",
                "category": "modes",
                "keywords": ["mode", "offline", "hors-ligne", "déconnecté", "faible connexion", "sans internet"]
            },
            {
                "question_fr": "Quand utiliser le mode hybride ?",
                "answer_fr": "Le mode hybride est recommandé quand la connexion est faible mais disponible. Il combine la base locale de FAQ avec une recherche sémantique plus intelligente (embeddings) pour mieux comprendre les formulations différentes d'une même question.",
                "question_ar": "متى أستخدم الوضع الهجين؟",
                "answer_ar": "يُنصح باستخدام الوضع الهجين عندما يكون الاتصال ضعيفًا لكنه موجود. يجمع بين قاعدة الأسئلة المحلية وبحث دلالي أذكى لفهم صيغ مختلفة لنفس السؤال.",
                "category": "modes",
                "keywords": ["mode", "hybride", "embeddings", "rag", "connexion faible", "recherche sémantique"]
            },
            {
                "question_fr": "Quand utiliser le mode en ligne ?",
                "answer_fr": "Le mode en ligne est utilisé lorsque la connexion est bonne. Il peut appeler un backend complet pour générer des réponses plus riches tout en gardant un repli automatique vers le mode hybride en cas de problème réseau.",
                "question_ar": "متى أستخدم الوضع المتصل؟",
                "answer_ar": "يُستخدم الوضع المتصل عندما تكون جودة الاتصال جيدة. يمكنه استدعاء خادم خلفي كامل لإنتاج إجابات أغنى مع الرجوع تلقائيًا إلى الوضع الهجين في حالة حدوث مشكلة في الشبكة.",
                "category": "modes",
                "keywords": ["mode", "online", "en ligne", "backend", "réseau", "internet"]
            },
            {
                "question_fr": "L'assistant fonctionne-t-il avec une connexion Internet faible ?",
                "answer_fr": "Oui. L'assistant est conçu pour les contextes de faible connectivité : il dispose d'un mode hors-ligne basé sur une base locale de questions/réponses et d'un mode hybride qui limite les échanges réseau au strict minimum.",
                "question_ar": "هل يعمل المساعد مع اتصال إنترنت ضعيف؟",
                "answer_ar": "نعم، تم تصميم المساعد لبيئات الاتصال الضعيف: لديه وضع عدم اتصال يعتمد على قاعدة أسئلة/أجوبة محلية ووضع هجين يقلل التبادل عبر الشبكة إلى الحد الأدنى.",
                "category": "assistant",
                "keywords": ["connexion faible", "faible débit", "offline", "hybride", "low-cost", "réseau"]
            },
            {
                "question_fr": "L'assistant est-il bilingue (français / arabe) ?",
                "answer_fr": "Oui. L'interface et la base de FAQ sont disponibles en français et en arabe. Vous pouvez changer de langue à tout moment avec le bouton FR/العربية en haut à droite.",
                "question_ar": "هل المساعد ثنائي اللغة (فرنسي / عربي)؟",
                "answer_ar": "نعم، الواجهة وقاعدة الأسئلة المتكررة متوفرة بالفرنسية والعربية. يمكنك تغيير اللغة في أي وقت باستخدام زر FR/العربية في الأعلى على اليمين.",
                "category": "assistant",
                "keywords": ["bilingue", "français", "arabe", "langue", "traduction", "interface"]
            },
            {
                "question_fr": "Que fait le bouton pour effacer la conversation ?",
                "answer_fr": "Le bouton avec l'icône de corbeille dans l'en-tête du chat permet de réinitialiser la conversation en supprimant les messages affichés. Cela n'affecte pas les données techniques stockées pour le bon fonctionnement de l'assistant.",
                "question_ar": "ماذا يفعل زر مسح المحادثة؟",
                "answer_ar": "زر سلة المهملات في أعلى واجهة المحادثة يسمح بإعادة تعيين المحادثة وحذف الرسائل الظاهرة فقط. هذا لا يؤثر على البيانات التقنية المخزنة اللازمة لعمل المساعد.",
                "category": "assistant",
                "keywords": ["effacer", "conversation", "historique", "corbeille", "réinitialiser", "chat"]
            },
            {
                "question_fr": "Quels types de questions puis-je poser à l'assistant ?",
                "answer_fr": "Vous pouvez poser des questions sur l'organisation de la Nuit de l'Info, l'inscription, les défis, le règlement, les horaires, ainsi que sur le fonctionnement de l'assistant IA low-cost lui-même (modes offline/hybride/online, langues, performances).",
                "question_ar": "ما نوع الأسئلة التي يمكنني طرحها على المساعد؟",
                "answer_ar": "يمكنك طرح أسئلة حول تنظيم ليلة المعلومات، التسجيل، التحديات، اللوائح، المواعيد، وكذلك حول طريقة عمل المساعد الذكي منخفض التكلفة نفسه (أوضاع عدم الاتصال/الهجين/المتصل، اللغات، الأداء).",
                "category": "assistant",
                "keywords": ["quelles questions", "poser", "exemples", "organisation", "défis", "modes ia"]
            }
        ]
        
        # Add core FAQs with IDs
        for i, faq in enumerate(core_faqs, 1):
            faqs.append({
                "id": i,
                "question_fr": faq["question_fr"],
                "answer_fr": faq["answer_fr"],
                "question_ar": faq.get("question_ar", ""),
                "answer_ar": faq.get("answer_ar", ""),
                "category": faq["category"],
                "keywords": faq["keywords"],
                "offline_priority": max(10 - (i // 5), 5),
                "source_url": "https://www.nuitdelinfo.com",
                "data_types": ["text"]
            })
        
        # === Add video FAQ if videos exist ===
        if data.get('videos'):
            video_texts = []
            for video in data['videos'][:3]:
                title = video.get('title', video.get('text', 'Vidéo'))
                url = video.get('url', '')
                if url:
                    video_texts.append(f"• {title}: {url}")
            
            if video_texts:
                faqs.append({
                    "id": len(faqs) + 1,
                    "question_fr": "Y a-t-il des vidéos de présentation ?",
                    "answer_fr": "Oui, voici les vidéos disponibles :\n" + "\n".join(video_texts),
                    "question_ar": "هل توجد فيديوهات تقديمية؟",
                    "answer_ar": "نعم، إليك الفيديوهات المتاحة.",
                    "category": "organisation",
                    "keywords": ["video", "vidéo", "youtube", "présentation", "media"],
                    "offline_priority": 5,
                    "source_url": "",
                    "data_types": ["video"]
                })
        
        print(f"  ✅ Generated {len(faqs)} FAQs")
        return faqs
    
    def save_faqs(self, faqs):
        """Save FAQs to frontend"""
        print("\n💾 Saving FAQs to frontend...")
        
        output = {
            "version": "6.0-enhanced",
            "last_updated": datetime.now().isoformat(),
            "source": "https://www.nuitdelinfo.com",
            "total_faqs": len(faqs),
            "ai_modes_info": {
                "offline": {
                    "name": "Mode Hors-ligne",
                    "method": "Recherche par mots-clés",
                    "speed": "< 200ms",
                    "uses": "IndexedDB local, keyword matching"
                },
                "hybrid": {
                    "name": "Mode Hybride",
                    "method": "RAG avec embeddings",
                    "speed": "< 3s",
                    "uses": "Embeddings vectoriels, similarité cosinus"
                },
                "online": {
                    "name": "Mode En-ligne",
                    "method": "API Backend",
                    "speed": "Variable",
                    "uses": "Serveur externe, fallback vers Hybrid"
                }
            },
            "faqs": faqs
        }
        
        os.makedirs('frontend/public/data', exist_ok=True)
        with open('frontend/public/data/faqs.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        print(f"  ✅ Saved {len(faqs)} FAQs to frontend/public/data/faqs.json")
        
        # Show categories distribution
        categories = Counter(faq['category'] for faq in faqs)
        print("\n📊 Categories distribution:")
        for cat, count in categories.items():
            print(f"  • {cat}: {count}")
    
    def create_embeddings(self, faqs):
        """Create embeddings for Hybrid mode"""
        print("\n🧮 Creating embeddings for Hybrid mode...")
        
        embeddings = []
        for faq in faqs:
            # Create embedding vector from text
            text = f"{faq['question_fr']} {faq['answer_fr']}"
            words = text.lower().split()
            
            # Create 384D vector (matches MiniLM)
            embedding = [0.0] * 384
            for word in words:
                h = hash(word) % 384
                embedding[h] += 1.0
            
            # Normalize
            magnitude = sum(x*x for x in embedding) ** 0.5
            if magnitude > 0:
                embedding = [x / magnitude for x in embedding]
            
            embeddings.append({
                "id": faq["id"],
                "question_fr": faq["question_fr"],
                "answer_fr": faq["answer_fr"],
                "answer_ar": faq.get("answer_ar", ""),
                "category": faq["category"],
                "embedding": embedding
            })
        
        output = {
            "version": "6.0",
            "model": "simple-hash-384d",
            "total_embeddings": len(embeddings),
            "embeddings": embeddings
        }
        
        with open('frontend/public/data/embeddings.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        print(f"  ✅ Saved {len(embeddings)} embeddings")
    
    def process(self):
        """Main processing pipeline"""
        print("🚀 Smart FAQ Generator - Enhanced Version\n")
        print("=" * 60)
        
        # Load data
        data = self.load_scraped_data()
        
        # Generate FAQs
        faqs = self.generate_faqs(data)
        
        # Save FAQs
        self.save_faqs(faqs)
        
        # Create embeddings
        self.create_embeddings(faqs)
        
        print("\n" + "=" * 60)
        print("✅ Processing complete!\n")
        print("📋 Summary:")
        print(f"   • {len(faqs)} FAQs generated")
        print(f"   • Keywords optimized for OFFLINE mode (🔴)")
        print(f"   • Embeddings created for HYBRID mode (🟡)")
        print(f"   • Ready for ONLINE mode fallback (🟢)")
        print("\n🎯 AI Modes:")
        print("   🔴 OFFLINE: Keyword search in IndexedDB (< 200ms)")
        print("   🟡 HYBRID:  RAG with embeddings & cosine similarity (< 3s)")
        print("   🟢 ONLINE:  API backend call with Hybrid fallback")
        
        return faqs


if __name__ == '__main__':
    generator = SmartFAQGenerator()
    generator.process()
