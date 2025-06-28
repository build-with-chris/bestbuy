# BestBuy App

**BestBuy** ist ein einfaches Python-Modul zur Verwaltung eines Warenkorbs mit verschiedenen Produkttypen.  
Es unterstützt Standard-Produkte, Nicht-Lagernde Produkte und auf Stückzahl begrenzte Produkte – inklusive Bestandsprüfung und Preisberechnung.

---

## Inhaltsverzeichnis

1. [Projektübersicht](#projektübersicht)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Verwendung](#verwendung)  
5. [API-Referenz](#api-referenz)  
6. [Beispiel](#beispiel)  
7. [Lizenz](#lizenz)

---

## Projektübersicht

Das **BestBuy-Modul** besteht aus drei Produktklassen und einer `Store`-Klasse:

- **`Product`** – Basisklasse mit `name`, `price` und `quantity`.  
- **`NonStockedProduct`** – Artikel, die keine Lagerbestände haben (z. B. Dienstleistungen).  
- **`LimitedProduct`** – Artikel mit festem Maximalbestand pro Bestellung.  
- **`Store`** – Verwaltet eine Liste von Produkten, prüft Bestände, und berechnet Gesamtpreise mit Promotionen.

---

## Features

- ✅ Produkte hinzufügen und entfernen  
- 📊 Gesamte Menge aller Artikel ermitteln  
- 📋 Nur aktive Produkte listen  
- ⚠️ Bestellvalidierung (Lagerbestand & Mengenlimits)  
- 💰 Gesamtpreis-Berechnung unter Berücksichtigung von Promotions

---

## Installation

1. Repository klonen  
   ```bash
   git clone https://github.com/dein-username/bestbuy_app.git
   cd bestbuy_app
