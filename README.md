# README.md

This repository contains various files related to the Synthetic Cognitive Augmentation Network (SCAN) project.

## Code

### SCANV1.ipynb

This Jupyter notebook contains the code for the SCAN system, including:

- Installation of required libraries (PyTorch, Transformers, Datasets, Weights & Biases)
- Importing necessary modules for model building, data loading, and logging
- Defining custom surrogate functions and classes for spiking neural networks
- Defining the Adaptive Exponential Integrate-and-Fire (AdEx) neuron model
- Defining the Spiking Neural Network (SNN) layer
- Defining a combined model using Transformers and SNN
- Defining training and saving functions for the model
- Loading and preprocessing the WikiText-2 dataset
- Training the combined model and saving the final weights and tokenizer

## Forms

### Synthetic Cognitive Augmentation Network Alignment Questionnaire.md

This markdown file contains the Synthetic Cognitive Augmentation Network Alignment Questionnaire (SCANAQ), which is designed to evaluate various aspects of a user's cognitive functioning and personal preferences to align the SCAN system with their unique needs. The questionnaire includes sections on:

- Executive Functioning
- Emotion Regulation
- Impulsivity
- Risk Propensity
- Decision-Making Style
- Self-Efficacy
- Perceived Stress
- Empathy and Social Cognition

The file also includes information on scoring, interpretation, privacy, and confidentiality.

### Cognitive Augmentation User Survey Evaluation.md

This markdown file contains the Cognitive Augmentation User Survey Evaluation (CAUSE), which aims to gather user insights to help develop the SCAN system to meet user needs and expectations. The survey consists of approximately 50 questions and covers topics such as:

- General User Requirements and Expectations
- Desired Use Cases and Applications
- Desired Features and Functionalities
- Perceived Value and Potential Benefits
- User Interface and Experience Preferences
- Technological Proficiency and Current Tool Usage
- Pain Points and Current Challenges
- Security and Privacy Concerns
- Accessibility and User Interface Preferences
- Demographic Information
- Pricing and Value Perception

### TrainingDatasets

This directory contains several JSON lines files for training and validation data related to different brain regions:

TrainingDatasets\acc_training_data.jsonl
TrainingDatasets\acc_validation_data.jsonl
TrainingDatasets\dlpfc_training_data.jsonl
TrainingDatasets\dlpfc_validation_data.jsonl
TrainingDatasets\mPFC_training_data.jsonl
TrainingDatasets\mPFC_validation_data.jsonl
TrainingDatasets\ofc_training_data.jsonl
TrainingDatasets\ofc_validation_data.jsonl
TrainingDatasets\vmpfc_training_data.jsonl
TrainingDatasets\vmpfc_validation_data.jsonl