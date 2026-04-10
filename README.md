# SSRR Frequency-to-Geometry Prediction Model

## 📌 Overview
This project presents a data-driven empirical model to predict the resonance frequency of Split Square Ring Resonators (SSRR) and enables inverse design of geometry for a target frequency.

The model is derived from simulation data and validated against electromagnetic simulations and classical LC resonance theory.

## 🎯 Objectives
- Predict resonance frequency from SSRR geometry
- Enable inverse design (geometry for target frequency)
- Compare with LC model (Pendry model)
- Generate dataset for ML/RF research

## 📐 Proposed Model

f = 64.28 * R_avg^-1.17 * gap^0.025 * width^0.05 * thickness^0.001

## 🛠 Tools Used
- Python (NumPy, Pandas, Matplotlib)
- CST Microwave Studio
- Data Analysis & Curve Fitting

## 📊 Features
- High accuracy (~0.3% error)
- Works from 1 GHz to 20 GHz
- Captures non-ideal EM effects beyond LC model

## 🔬 Future Work
- LC model comparison and validation
- Machine learning extension
- Real-world fabrication validation

## 📁 Project Structure
(To be updated)

## 👨‍🔬 Author
Annanya Mishra
