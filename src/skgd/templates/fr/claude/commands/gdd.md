# /gdd - Générer le Game Design Document

Vous êtes Opus, générant un Document de Conception de Jeu formel qui synthétise tout le travail de design.

## Modèle

**OBLIGATOIRE : opus** - La synthèse de documents nécessite une compréhension complète et une organisation créative.

## Langue

Lire `.skgd/config.yaml` → `user.language`
Utiliser `.skgd/i18n/messages.yaml` pour le texte utilisateur.

## Objectif

Générer un GDD formel et partageable qui synthétise :
- La vision de `game-brief.md`
- Les décisions de design de `pillars/*.md`
- L'approche technique de `architecture.md`
- La portée d'implémentation de `roadmap.yaml`

**Sortie :** `docs/gdd.md`

---

## Quand l'utiliser

- Après que tous les pillars sont complets (idéal)
- Après que `/validate-design` passe
- À tout moment comme checkpoint de synthèse
- Avant de partager avec les parties prenantes/équipe

---

## Phase 0 : Reconnaissance du Contexte

**AVANT toute autre étape**, rassembler tout le contexte de design via un sous-agent Scout :

Utiliser l'outil Task :
- subagent_type: 'Explore'
- model: 'haiku'
- prompt: |
    Reconnaissance de tous les documents de design pour la génération du GDD :

    1. Lire docs/game-brief.md - extraire :
       - Titre du jeu, genre, audience cible
       - Déclaration de concept (pitch)
       - USPs (arguments de vente uniques)
       - Expérience/émotions cibles
       - Plateforme(s)

    2. Lire docs/pillars/_index.md - obtenir la liste des pillars et leur statut

    3. Pour chaque pillar COMPLÉTÉ dans docs/pillars/, extraire :
       - Nom du pillar
       - 2-3 décisions clés avec justification
       - Mécaniques/systèmes principaux définis
       - Références mentionnées

    4. Lire docs/architecture.md (si existe) - extraire :
       - Stack technique
       - Patterns clés
       - Objectifs de performance

    5. Lire .skgd/roadmap.yaml (si existe) - extraire :
       - Liste des features MVP
       - Total des features planifiées
       - Structure des cycles

    6. Lire .skgd/memory/constitution.md - extraire les principes de design

    Retourner le format Rapport Scout (max 800 tokens, c'est une synthèse) :

    ## Rapport Scout : gdd
    **Statut :** ready | partial | blocked

    **Identité du Jeu :**
    - Titre : [nom]
    - Genre : [genre]
    - Plateforme : [plateformes]
    - Pitch : [concept en 1-2 phrases]

    **Statut des Pillars :** [N]/[M] complets

    **Décisions Clés par Pillar :**
    - [pillar-1] : [résumé des décisions]
    - [pillar-2] : [résumé des décisions]
    - ...

    **Mécaniques Principales :**
    - [mécanique 1] : [bref]
    - [mécanique 2] : [bref]

    **Stack Technique :** [résumé]

    **Portée :**
    - MVP : [liste des features]
    - Complet : [N features sur M cycles]

    **Principes de Design :** [depuis constitution]

    **Manquant :** [fichiers non trouvés ou "aucun"]

**SI Scout retourne "blocked" :** Le minimum requis est game-brief.md. Si manquant, router vers `/brainstorm`.
**SI Scout retourne "partial" :** Procéder avec l'info disponible, noter les lacunes dans le GDD.

---

## Étape 1 : Vérifier la Complétude

```
Vérification de Génération du GDD

Documents de Design Trouvés :
✅ game-brief.md - Vision principale
[✅|⬜] pillars/ - [N]/[M] complets
[✅|⬜] architecture.md - Design technique
[✅|⬜] roadmap.yaml - Portée/priorités

Recommandation :
[Si tout complet] : "Prêt à générer un GDD complet"
[Si partiel] : "Peut générer un GDD avec lacunes notées. Manquant : [liste]"
```

Demander à l'utilisateur :
```
Procéder avec la génération du GDD ?
  [A] Oui, générer maintenant
  [B] Laissez-moi compléter plus de pillars d'abord
```

---

## Étape 2 : Générer le GDD

Transformer le Rapport Scout + lectures ciblées en structure GDD formelle :

```markdown
# [Titre du Jeu] - Game Design Document

> [Pitch depuis game-brief]

## Info Document
- **Version :** 1.0
- **Généré :** [timestamp]
- **Statut :** [Brouillon/En Cours/Complet]
- **Pillars Complets :** [N]/[M]

---

## 1. Aperçu du Jeu

### 1.1 Déclaration de Concept
[Expansion depuis le concept game-brief]

### 1.2 Genre
[Genre principal] avec [éléments secondaires]

### 1.3 Audience Cible
- **Âge :** [depuis game-brief]
- **Type de Joueur :** [casual/core/hardcore]
- **Intérêts :** [ce qu'ils apprécient]

### 1.4 Arguments de Vente Uniques
1. [USP 1 depuis game-brief]
2. [USP 2]
3. [USP 3]

### 1.5 Plateforme(s)
- Principale : [plateforme]
- Secondaire : [si applicable]

### 1.6 Principes de Design
[Depuis constitution.md]
1. [Principe 1]
2. [Principe 2]
3. [Principe 3]

---

## 2. Gameplay

### 2.1 Boucle Principale
[Depuis pillar game-loop ou game-brief]
```
[Action] → [Feedback] → [Récompense] → [Progression] → [Action]
```

### 2.2 Mécaniques Principales

#### [Nom Mécanique 1]
*Source : pillar [nom-pillar]*

- **Description :** [depuis décisions pillar]
- **Contrôles :** [si défini]
- **Objectif de Ressenti :** [depuis pillar]
- **Décision Clé :** [justification depuis pillar]

#### [Nom Mécanique 2]
*Source : pillar [nom-pillar]*

- **Description :** [depuis pillar]
- **Contrôles :** [si défini]
- **Objectif de Ressenti :** [depuis pillar]
- **Décision Clé :** [justification]

### 2.3 Objectifs de Game Feel
| Aspect | Objectif | Référence |
|--------|----------|-----------|
| [Aspect 1] | [Objectif] | [Référence jeu depuis pillars] |
| [Aspect 2] | [Objectif] | [Référence] |

---

## 3. Progression

### 3.1 Type de Progression
[Depuis pillar progression ou game-brief]

### 3.2 Courbe de Progression
[Depuis décisions pillar]

### 3.3 Déblocages & Récompenses
[Depuis pillar]

---

## 4. Univers de Jeu

### 4.1 Cadre
[Depuis pillar art-direction ou player-experience]

### 4.2 Style Visuel
- **Direction Artistique :** [depuis pillar]
- **Palette de Couleurs :** [depuis pillar]
- **Ambiance :** [depuis pillar]

### 4.3 Direction Audio
[Depuis pillar si existe, sinon noter comme À DÉFINIR]

---

## 5. Niveaux/Mondes

### 5.1 Structure
[Depuis pillar level-design]

### 5.2 Principes de Level Design
[Depuis décisions pillar]

---

## 6. Personnages/Entités

[Depuis pillars pertinents - enemy-design, character-progression, etc.]

---

## 7. UI/UX

### 7.1 Philosophie HUD
[Depuis pillar player-experience]

### 7.2 Objectifs d'Accessibilité
[Depuis game-brief ou pillar]

---

## 8. Specs Techniques

*Source : architecture.md*

### 8.1 Stack Technologique
- Moteur : [Unity/Godot]
- Langage : [C#/GDScript]
- Patterns Clés : [depuis architecture]

### 8.2 Performance Cible
| Plateforme | FPS | Résolution |
|------------|-----|------------|
| [Plateforme] | [Cible] | [Cible] |

### 8.3 Système de Sauvegarde
[Depuis architecture]

---

## 9. Portée & Jalons

*Source : roadmap.yaml*

### 9.1 Features MVP (Cycle 1)
- [ ] [Feature 1]
- [ ] [Feature 2]
- [ ] [Feature 3]

### 9.2 Features Version Complète
[Cycles 2+ depuis roadmap]

### 9.3 Idées Post-Launch
[Depuis objectifs stretch roadmap]

---

## 10. Références

### 10.1 Références de Jeux
[Agrégées depuis tous les pillars]

| Jeu | Ce Qu'on Prend | Source Pillar |
|-----|----------------|---------------|
| [Jeu] | [Élément] | [nom-pillar] |

---

## 11. Risques & Mitigation

[Agrégés depuis sections risques des pillars]

| Risque | Source | Mitigation |
|--------|--------|------------|
| [Risque] | [pillar] | [Stratégie] |

---

## 12. Questions Ouvertes

[Agrégées depuis questions ouvertes des pillars]

- [ ] [Question depuis pillar-1]
- [ ] [Question depuis pillar-2]

---

## Annexe A : Résumé des Pillars

| Pillar | Statut | Décisions Clés |
|--------|--------|----------------|
| [pillar-1] | ✅ Complet | [Décisions] |
| [pillar-2] | ✅ Complet | [Décisions] |
| [pillar-3] | ⬜ Stub | - |

---

## Annexe B : Journal des Décisions

| Décision | Choix | Justification | Pillar |
|----------|-------|---------------|--------|
| [Question] | [Réponse] | [Pourquoi] | [Source] |

---

*Généré par SKGD v3.5*
*Source : docs/game-brief.md, docs/pillars/*.md, docs/architecture.md, .skgd/roadmap.yaml*
*Voir aussi : docs/pillars/_index.md pour détails des pillars*
```

---

## Étape 3 : Écrire le GDD

Écrire dans `docs/gdd.md`

---

## Étape 4 : Mettre à Jour l'État

Mettre à jour `.skgd/state.yaml` :
```yaml
gdd:
  generated: true
  version: 1.0
  timestamp: [ISO-8601]
  pillars_at_generation: [N]/[M]
```

---

## Étape 5 : Commit Git

```bash
git add docs/gdd.md
git commit -m "docs: génération GDD v1.0

Synthétisé depuis :
- game-brief.md
- [N] pillars
- architecture.md
- roadmap.yaml

Pillars complets : [N]/[M]"
```

---

## Étape 6 : Résumé

```
📄 Game Design Document Généré

docs/gdd.md créé (v1.0)

Résumé du Contenu :
• Sections : 12 + 2 annexes
• Pillars synthétisés : [N]/[M]
• Mécaniques documentées : [nombre]
• Références consolidées : [nombre]
• Questions ouvertes : [nombre]

Statut du Document :
[Si tous pillars complets] : COMPLET - Prêt à partager
[Si partiel] : BROUILLON - Lacunes notées, mettre à jour après plus de pillars

Prochaines Étapes :
  - Réviser et affiner manuellement si nécessaire
  - Partager avec l'équipe/parties prenantes
  - Relancer /gdd après avoir complété plus de pillars
```

---

## Régénération

Relancer `/gdd` va :
- Écraser le `docs/gdd.md` existant
- Incorporer les nouvelles complétions de pillars
- Mettre à jour la version et le timestamp

---

## Anti-Patterns

```
MAUVAIS : Générer le GDD avec zéro pillar complété
BON : Au moins game-brief et 2-3 pillars

MAUVAIS : Copier le texte des pillars textuellement
BON : Synthétiser et organiser en structure GDD

MAUVAIS : Laisser des placeholders [comme ceci]
BON : Marquer les sections comme "À DÉFINIR - nécessite [pillar]" si info manquante

MAUVAIS : Inventer du contenu absent des docs sources
BON : Synthétiser uniquement ce qui existe, noter les lacunes
```

---

*Version : 3.5*
*Pattern : Scout-First pour la collecte de contexte*
