# PasseInfo SDK
# ![PASSEINFO](https://api.passinfo.net/v1/content/logo.png "PasseInfo Logo")

Un SDK Python puissant et intuitif pour une intégration transparente avec l'API PasseInfo, permettant une livraison de messages rapide, fiable et sécurisée à travers plusieurs canaux. Ce SDK simplifie les opérations de messagerie complexes en un code propre et maintenable, en faisant le choix idéal pour les entreprises recherchant des solutions de communication robustes.

## 1️⃣ Description

PasseInfo SDK est une bibliothèque Python puissante et conviviale conçue pour simplifier l'intégration des services de messagerie PasseInfo dans vos applications. Ce SDK abstrait la complexité des interactions directes avec l'API, offrant une interface propre et intuitive pour l'envoi de messages à travers différents canaux.

Le SDK gère toute l'authentification API nécessaire, le formatage des requêtes et l'analyse des réponses, permettant aux développeurs de se concentrer sur l'implémentation de leur logique de messagerie plutôt que de gérer les détails de bas niveau de l'API. Il fournit une gestion robuste des erreurs, des tentatives automatiques pour les requêtes échouées et des capacités complètes de journalisation.

Les principaux avantages de l'utilisation du SDK PasseInfo incluent :
- **Intégration Simplifiée** : Méthodes faciles à utiliser pour toutes les opérations de messagerie
- **Sécurité des Types** : Validation intégrée pour tous les paramètres API
- **Configuration Flexible** : Paramètres personnalisables pour différents cas d'utilisation
- **Prêt pour la Production** : Testé en conditions réelles dans des scénarios à haut volume
- **Bien Documenté** : Documentation complète avec des exemples pratiques
- **Utilisation Efficace des Ressources** : Optimisé pour gérer les messages uniques et en masse

Que vous envoyiez des messages transactionnels, des communications marketing ou des notifications système, PasseInfo SDK fournit les outils et la flexibilité dont vous avez besoin pour implémenter des fonctionnalités de messagerie robustes dans vos applications Python.

## 2️⃣ Fonctionnalités

- Envoi de messages individuels aux contacts
- Envoi en masse de messages à plusieurs contacts simultanément
- Envoi de messages à des groupes de contacts prédéfinis
- Suivi du statut de livraison des messages individuels et en masse
- Surveillance des statuts des lots de messages et rapports de livraison
- Gestion complète des erreurs
- Formatage et validation automatiques des requêtes
- Authentification API sécurisée

## 3️⃣ Installation

Le SDK PasseInfo peut être facilement installé via pip, le gestionnaire de paquets Python. Le SDK est compatible avec tous les principaux systèmes d'exploitation (Windows, macOS, Linux) et nécessite un minimum de dépendances. Avant l'installation, assurez-vous d'avoir Python 3.6 ou une version supérieure installée sur votre système.

### 3️⃣.1️⃣ Prérequis

- Python 3.6 ou supérieur
- Bibliothèque `requests`

### 3️⃣.2️⃣ Installation via pip

```bash
pip install passinfo-sdk
```

## 4️⃣ Démarrage Rapide

Cette section vous guidera à travers les étapes essentielles pour commencer à utiliser le SDK PasseInfo dans votre application. Vous apprendrez à initialiser le client, envoyer des messages à des contacts individuels, des groupes, et gérer efficacement plusieurs destinataires. Avant de commencer, assurez-vous d'avoir :

- Installé le package SDK PasseInfo
- Obtenu vos identifiants API depuis le tableau de bord PasseInfo
- Une compréhension basique de la programmation Python

### 4️⃣.1️⃣ Initialiser le Client

Créez une nouvelle instance du client SDK PasseInfo avec vos identifiants API. Vous pouvez obtenir ces identifiants depuis votre tableau de bord PasseInfo :

> **Note** : Gardez vos identifiants API sécurisés et ne les exposez jamais dans votre code. Utilisez des variables d'environnement ou une gestion de configuration sécurisée pour les déploiements en production.

Voici comment initialiser le client :

```python
from passinfo_sdk import PassInfoSDKClient

client = PassInfoSDKClient(
    api_key="your_api_key",    # Votre clé API PasseInfo
    client_id="your_client_id" # Votre ID client PasseInfo
)
```

### 4️⃣.2️⃣ Envoyer un Message Unique

Envoyez un message à un contact individuel. Cette méthode fournit un moyen simple de livrer des messages à des destinataires spécifiques :

```python
response = client.send_message(
    message="Hello World",           # Contenu du message
    contact="phoneNumber",          # Numéro de téléphone du destinataire
    sender_name="senderName"       # Nom qui apparaît comme expéditeur
)
print(response)
# Exemple de sortie : {"status": "success", "message": "123"}
```

#### 4️⃣.2️⃣.1️⃣ Paramètres
- `message` (str) : Le contenu de votre message. Gardez-le clair et concis.
- `contact` (str) : Le numéro de téléphone du destinataire dans un format valide (ex : "622000001").
- `sender_name` (str) : Votre ID d'expéditeur que les destinataires verront.

#### 4️⃣.2️⃣.2️⃣ Réponse
La méthode renvoie un dictionnaire contenant :
- `status` : Statut de succès ou d'échec de l'opération d'envoi
- `message` : Identifiant unique pour le suivi du message

#### 4️⃣.2️⃣.3️⃣ Meilleures Pratiques
- Validez les numéros de téléphone avant l'envoi
- Gardez le contenu du message dans les limites de caractères
- Stockez le message_id pour le suivi des livraisons
- Gérez les erreurs API potentielles en utilisant des blocs try-except

### 4️⃣.3️⃣ Envoi de Messages en Masse

Envoyez un message à plusieurs contacts simultanément. Cette méthode fournit un moyen efficace de livrer le même message à plusieurs destinataires en un seul appel API :

```python
contacts = ["622000001", "622000002", "622000003"]
response = client.send_message_bulk(
    message="Hello Everyone",        # Contenu du message
    sender_name="senderName",       # Nom qui apparaît comme expéditeur
    contacts=contacts               # Liste des numéros de téléphone des destinataires
)
print(response)
# Exemple de sortie : {"status": "success", "successful_sends": 3, "failed_sends": 0}
```

#### 4️⃣.3️⃣.1️⃣ Paramètres
- `message` (str) : Le contenu de votre message qui sera envoyé à tous les destinataires.
- `sender_name` (str) : Votre ID d'expéditeur qui apparaîtra comme expéditeur pour tous les destinataires.
- `contacts` (list) : Une liste de numéros de téléphone auxquels envoyer le message.

#### 4️⃣.3️⃣.2️⃣ Réponse
La méthode renvoie un dictionnaire contenant :
- `status` : Statut de succès ou d'échec de l'opération d'envoi en masse
- `successful_sends` : Nombre de messages mis en file d'attente avec succès pour la livraison
- `failed_sends` : Nombre de messages qui n'ont pas pu être mis en file d'attente

#### 4️⃣.3️⃣.3️⃣ Meilleures Pratiques
- Gardez la taille de la liste de contacts raisonnable pour éviter les délais d'attente
- Validez tous les numéros de téléphone avant l'envoi
- Surveillez la réponse pour les envois échoués
- Implémentez une logique de réessai pour les livraisons échouées

### 4️⃣.4️⃣ Envoi de Message à un Groupe

Envoyez un message à un groupe prédéfini de contacts. Cette méthode vous permet de livrer efficacement des messages à des groupes qui ont été créés et gérés via votre tableau de bord PasseInfo :

```python
response = client.send_message_group(
    message="Hello Group",           # Contenu du message
    sender_name="senderName",       # Nom qui apparaît comme expéditeur
    group_id="groupId"             # ID du groupe cible
)
print(response)
# Exemple de sortie : {"status": "success", "group_size": 50, "messages_queued": 50}
```

#### 4️⃣.4️⃣.1️⃣ Paramètres
- `message` (str) : Le contenu de votre message qui sera envoyé à tous les membres du groupe.
- `sender_name` (str) : Votre ID d'expéditeur qui apparaîtra comme expéditeur pour tous les membres du groupe.
- `group_id` (str) : L'identifiant unique de votre groupe cible (disponible dans le tableau de bord PasseInfo).

#### 4️⃣.4️⃣.2️⃣ Réponse
La méthode renvoie un dictionnaire contenant :
- `status` : Statut de succès ou d'échec de l'opération d'envoi au groupe
- `group_size` : Nombre total de contacts dans le groupe
- `messages_queued` : Nombre de messages mis en file d'attente avec succès pour la livraison

#### 4️⃣.4️⃣.3️⃣ Meilleures Pratiques
- Vérifiez l'existence du groupe avant l'envoi
- Gardez les tailles de groupe gérables
- Surveillez le statut de livraison pour les grands groupes
- Tenez compte des fuseaux horaires pour le timing des messages

### 4️⃣.5️⃣ Obtenir le Statut d'un Message

Suivez le statut de livraison d'un message unique en utilisant son ID unique :

```python
response = client.get_message_status(
    message_id="1234567890"        # Identifiant unique du message
)
print(response)
# Exemple de sortie : {"status": "sent", "message_id": "1234567890"}
```

#### 4️⃣.5️⃣.1️⃣ Paramètres
- `message_id` (str) : L'identifiant unique du message à suivre, retourné lors de l'envoi du message.

#### 4️⃣.5️⃣.2️⃣ Réponse
La méthode renvoie un dictionnaire contenant :
- `status` : Statut actuel du message (ex : 'pending', 'sent', 'failed')
- `message_id` : L'identifiant unique du message suivi

#### 4️⃣.5️⃣.3️⃣ Meilleures Pratiques
- Stockez les ID des messages pour les communications importantes
- Implémentez une interrogation du statut à intervalles appropriés
- Gérez tous les statuts possibles dans votre application

### 4️⃣.6️⃣ Obtenir le Statut des Messages en Masse

Suivez le statut de livraison de plusieurs messages envoyés en lot :

```python
response = client.get_message_status_bulk(
    batch_id="1234567890"         # Identifiant unique du lot
)
print(response)
# Exemple de sortie : {"status": "processing", "successful": 45, "failed": 2, "pending": 3}
```

#### 4️⃣.6️⃣.1️⃣ Paramètres
- `batch_id` (str) : L'identifiant unique du lot de messages à suivre.

#### 4️⃣.6️⃣.2️⃣ Réponse
La méthode renvoie un dictionnaire contenant :
- `status` : Statut général du lot
- `successful` : Nombre de messages livrés avec succès
- `failed` : Nombre de livraisons échouées
- `pending` : Nombre de messages encore en file d'attente

#### 4️⃣.6️⃣.3️⃣ Meilleures Pratiques
- Stockez les ID de lot pour les opérations en masse
- Implémentez une logique de réessai pour les messages échoués
- Surveillez les taux et les modèles de livraison
- Configurez des alertes pour les taux d'échec élevés

## 5️⃣ Gestion des Erreurs

Le SDK fournit une gestion complète des erreurs via l'exception `PassInfoAPIError` :

```python
from passinfo_sdk.exceptions import PassInfoAPIError

try:
    response = client.send_message(
        message="Hello World",
        contact="phoneNumber",
        sender_name="senderName"
    )
except PassInfoAPIError as e:
    print(f"Erreur {e.status_code}: {e.message}")
```

### 5️⃣.1️⃣ Vérifier le Solde de Crédits SMS

Vérifiez le solde de crédits SMS restant pour votre compte :

```python
try:
    remaining_credits = client.get_sms_count()
    print(f"Il vous reste {remaining_credits} crédits SMS")
except PassInfoAPIError as e:
    print(f"Erreur lors de la vérification du solde SMS : {e}")
```

#### 5️⃣.2️⃣ Retourne
- `int` : Le nombre de crédits SMS restants sur le compte. Retourne 0 si la requête échoue ou s'il n'y a pas de crédits disponibles.

#### 5️⃣.3️⃣ Meilleures Pratiques
- Implémentez des vérifications régulières du solde pour assurer des crédits suffisants
- Configurez des alertes de solde bas dans votre application
- Gérez les erreurs API potentielles avec élégance
- Envisagez d'implémenter des mécanismes de recharge automatique de crédits
- Surveillez les modèles d'utilisation des crédits pour la planification de la capacité

 
### 5️⃣.4️⃣ Renouvellement de la Clé API

Faites pivoter votre clé API pour une sécurité renforcée en utilisant la méthode renew_api_key. Cette opération invalide votre clé API actuelle et en génère une nouvelle :

```python
try:
    response = client.renew_api_key()
    if response.get('api_key'):
        new_key = response['api_key']
        print(f"Nouvelle clé API générée avec succès")
        # Mettez à jour votre configuration avec la nouvelle clé
    else:
        print("Échec de la génération de la nouvelle clé API")
except PasseInfoAPIError as e:
    print(f"Erreur lors du renouvellement de la clé API : {e}")
```

#### 5️⃣.5️⃣ Retours
- `dict` : Contient la nouvelle clé API dans la réponse
  - `api_key` (str) : La clé API nouvellement générée

#### Meilleures Pratiques
- Planifier des rotations régulières des clés (par exemple, tous les 90 jours)
- Mettre en œuvre des périodes de transition appropriées
- Stocker les nouvelles clés de manière sécurisée (par exemple, variables d'environnement)
- Mettre à jour toutes les instances d'application avec la nouvelle clé
- Maintenir un accès de secours pendant la rotation
- Journaliser tous les événements de rotation des clés

#### Directives d'Implémentation
1. **Préparation**
   - Sauvegarder la configuration actuelle
   - Planifier une fenêtre de maintenance si nécessaire
   - S'assurer que tous les systèmes sont prêts pour la mise à jour

2. **Exécution**
   - Générer une nouvelle clé API
   - Valider la fonctionnalité de la nouvelle clé
   - Mettre à jour les fichiers/variables de configuration
   - Redémarrer les services affectés si nécessaire

3. **Vérification**
   - Tester la connectivité API avec la nouvelle clé
   - Surveiller les erreurs d'authentification
   - Vérifier que tous les systèmes fonctionnent

4. **Plan de Retour en Arrière**
   - Garder l'ancienne clé temporairement accessible
   - Documenter les procédures de retour en arrière
   - Mettre en place une surveillance des problèmes

#### Considérations de Sécurité
- Ne jamais journaliser ou afficher les clés API complètes
- Utiliser des canaux sécurisés pour la distribution des clés
- Mettre en œuvre un accès avec privilèges minimaux
- Surveiller l'utilisation non autorisée des clés
- Configurer des alertes pour les événements liés aux clés

#### Exemple d'Implémentation
```python
from passinfo_sdk import PasseInfoSDKClient
from passinfo_sdk.exceptions import PasseInfoAPIError
import os

def rotate_api_key(client):
    try:
        # Générer une nouvelle clé
        response = client.renew_api_key()
        if not response.get('api_key'):
            raise ValueError("Pas de clé API dans la réponse")

        new_key = response['api_key']
        
        # Valider la nouvelle clé
        test_client = PasseInfoSDKClient(
            api_key=new_key,
            client_id=client.client_id
        )
        
        # Tester la nouvelle clé
        test_client.get_sms_count()
        
        # Mettre à jour la configuration
        update_api_key_config(new_key)
        
        print("Clé API pivotée avec succès")
        return True
        
    except PasseInfoAPIError as e:
        print(f"Erreur lors de la rotation de la clé API : {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return False

def update_api_key_config(new_key):
    # Mettre à jour la variable d'environnement
    os.environ['PASSINFO_API_KEY'] = new_key
    
    # Mettre à jour le fichier de configuration
    # Implémentez votre logique de mise à jour de configuration ici
    pass

```
## Meilleures Pratiques
   
### Gestion des Messages

- Implémenter une file d'attente de messages pour les scénarios à haut volume
- Utiliser le traitement par lots pour optimiser les performances
- Mettre en place des mécanismes de réessai avec backoff exponentiel
- Implémenter le suivi du statut de livraison des messages
- Gérer la priorité des messages selon les besoins métier
- Valider le contenu des messages avant l'envoi

### Optimisation des Performances

- Utiliser le pooling de connexions pour une meilleure gestion des ressources
- Implémenter la mise en cache des données fréquemment utilisées
- Optimiser les tailles de lots pour les opérations en masse
- Surveiller et ajuster les limites de requêtes concurrentes
- Utiliser des opérations asynchrones lorsque possible
- Mettre en place une gestion efficace des timeouts
- Optimiser les requêtes pour minimiser la latence
- Implémenter des mécanismes de compression des données
- Utiliser des connexions persistantes
- Mettre en cache les résultats des requêtes fréquentes

### Sécurité et Conformité

- Implémenter le chiffrement des données sensibles
- Suivre les meilleures pratiques de sécurité pour le stockage des identifiants
- Respecter les réglementations sur la protection des données
- Mettre en place une journalisation sécurisée
- Effectuer des audits réguliers de sécurité
- Maintenir des sauvegardes sécurisées des données critiques

### Support et Maintenance

- Maintenir une documentation à jour
- Fournir des exemples de code pour les cas d'utilisation courants
- Offrir un support technique réactif
- Mettre à jour régulièrement les dépendances
- Suivre les bonnes pratiques de versioning
- Communiquer clairement les changements d'API
