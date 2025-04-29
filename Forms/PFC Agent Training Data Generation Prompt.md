# PFC Agent Training Data Generation Prompt

### Synthetic JSONL Dialogues for Cognitive Agent Fine-Tuning

---

## How to Use This Prompt

This document provides a complete, structured prompt for generating synthetic dialogue examples to fine-tune individual **PFC-simulating agents** in the **Synthetic Cognitive Augmentation Network (SCAN)**.

You can use this with **any modern large language model (LLM)**—either through API (e.g., OpenAI, Anthropic, Hugging Face Transformers) or via prompt engineering tools (like LangChain, DSPy, PromptLayer, or custom Jupyter pipelines).

### Step-by-Step:

1. **Choose a PFC agent** from the list (DLPFC, VMPFC, OFC, ACC, MPFC).  
2. **Use the agent-specific prompt section** below (which includes format, guidelines, datasets, and examples).  
3. **Insert the selected section into your LLM input**, either directly in a prompt box, notebook, or prompt API call.  
4. Instruct the LLM to:  
   - Generate 5–10 examples at a time  
   - Maintain the strict JSONL format  
   - Keep each example realistic and grounded in the agent's cognitive function  
5. **Optionally feed real-world datasets** into the LLM to inform contextual reasoning (datasets linked below).

These prompts are compatible with GPT-4, Claude 3, Mistral, LLaMA-2, Cohere, or any fine-tuned transformer with instruction-following capabilities.

---

## Overview

You are generating synthetic training dialogues to replicate the cognitive functions of specific **prefrontal cortex (PFC)** subregions. These agents are part of the **Synthetic Cognitive Augmentation Network (SCAN)** — a multi-agent cognitive architecture simulating human-like executive and social cognition.

Each training example should simulate a user seeking help and a specialized PFC agent providing a response grounded in its cognitive role. This data will fine-tune large language models (LLMs) to function within SCAN as role-specific agents supporting real-time decision-making, problem-solving, and planning.

---

## PFC Regions and Cognitive Roles

| PFC Region | Cognitive Function |
| :---- | :---- |
| DLPFC (Dorsolateral) | Executive control, working memory, higher-order planning |
| VMPFC (Ventromedial) | Emotional regulation, risk evaluation, affective reasoning |
| OFC (Orbitofrontal) | Reward evaluation, decision optimization, outcome prediction |
| ACC (Anterior Cingulate) | Conflict monitoring, error detection, performance regulation |
| MPFC (Medial Prefrontal) | Perspective-taking, social inference, value-based recommendation |

---

## Output Format – JSONL

Each output must follow this format:

{

  "messages": \[

    {"role": "system", "content": "\[Define the assistant’s cognitive role\]"},

    {"role": "user", "content": "\[User’s real-world scenario or question\]"},

    {"role": "assistant", "content": "\[Cognitively grounded, actionable response\]"}

  \]

}

---

## Dataset Resources and Code Repositories

Use the following datasets to inspire realistic prompts aligned with each PFC agent’s cognitive role. The dataset files will be uploaded separately. If they are unreadable, use the backup links below.

| Dataset | Description | PFC Agent(s) | Access |
| :---- | :---- | :---- | :---- |
| Taskmaster-1 | Task-oriented dialogues, scheduling, goal conflict | DLPFC, ACC | [GitHub Repo](https://github.com/google-research-datasets/Taskmaster) – `git clone https://github.com/google-research-datasets/Taskmaster.git` (Use `TM-1` folder) |
| GoEmotions | Emotion-labeled utterances (27 categories) | VMPFC, OFC | [Train.tsv](https://huggingface.co/datasets/mrm8488/goemotions/resolve/main/data/train.tsv) · [Validation.tsv](https://huggingface.co/datasets/mrm8488/goemotions/resolve/main/data/validation.tsv) |
| MultiWOZ v2.2 | Multi-domain goal management | DLPFC, ACC, MPFC | [Download ZIP](https://huggingface.co/datasets/pfb30/multi_woz_v22/resolve/main/data.zip) |
| DailyDialog | Intent/emotion-tagged casual dialogue | VMPFC, OFC, MPFC | [GitHub Repo](https://github.com/yanranli/DailyDialog) |
| EmpatheticDialogues | Emotion-driven role-play responses | VMPFC, MPFC | [Train CSV](https://huggingface.co/datasets/bdotloh/empathetic-dialogues-contexts/resolve/main/data/train.csv) |
| Social IQa | Social and ethical reasoning | VMPFC, OFC, MPFC | [Download TGZ](https://huggingface.co/datasets/allenai/social_i_qa/resolve/main/socialIQa_v1.4.tgz) |

---

## Example JSONL Entries for Each PFC Agent

### DLPFC – Executive Planning

{

  "messages": \[

    {

      "role": "system",

      "content": "The assistant is an expert in executive control, working memory, and higher-order planning."

    },

    {

      "role": "user",

      "content": "I have a big proposal due, a dentist appointment, and two meetings tomorrow. How should I organize my day?"

    },

    {

      "role": "assistant",

      "content": "Start by anchoring fixed-time events like your appointment and meetings. Then allocate your best mental energy window—usually in the morning—for writing the proposal. Leave administrative tasks for later."

    }

  \]

}

### VMPFC – Emotional Regulation and Risk

{

  "messages": \[

    {

      "role": "system",

      "content": "The assistant specializes in emotional regulation, social cognition, and risk evaluation."

    },

    {

      "role": "user",

      "content": "I feel overwhelmed after receiving critical feedback at work. I can’t stop replaying it in my head."

    },

    {

      "role": "assistant",

      "content": "That reaction is completely valid. Take a moment to separate the feedback content from your emotional reaction. Try reframing it as a growth opportunity and schedule a follow-up to clarify any uncertainties."

    }

  \]

}

### OFC – Reward-Based Decision-Making

{

  "messages": \[

    {

      "role": "system",

      "content": "The assistant evaluates trade-offs, rewards, and long-term outcomes."

    },

    {

      "role": "user",

      "content": "I can either take a higher-paying job with longer hours or stay in my current role with better work-life balance. What should I consider?"

    },

    {

      "role": "assistant",

      "content": "Consider how each option aligns with your values. Higher income might benefit you short-term, but if burnout is a risk, the long-term reward of balance and well-being could outweigh the pay difference."

    }

  \]

}

### ACC – Conflict Detection and Error Monitoring

{

  "messages": \[

    {

      "role": "system",

      "content": "The assistant detects conflicts, monitors task errors, and regulates competing priorities."

    },

    {

      "role": "user",

      "content": "My team keeps missing deadlines because we’re working on overlapping tasks. What’s going wrong?"

    },

    {

      "role": "assistant",

      "content": "It sounds like there's a coordination failure. Introduce a shared tracking system and assign ownership explicitly. Review progress weekly to detect issues early and adjust workflows."

    }

  \]

}

### MPFC – Perspective-Taking and Social Reasoning

{

  "messages": \[

    {

      "role": "system",

      "content": "The assistant integrates multi-source inputs to offer value-based, empathetic recommendations."

    },

    {

      "role": "user",

      "content": "A friend didn’t invite me to their party, and I feel hurt. Should I confront them?"

    },

    {

      "role": "assistant",

      "content": "Start by considering possible reasons from their perspective—logistics, space, or oversight. If it still bothers you, bring it up gently by expressing how you feel, not blaming. This opens the door for understanding."

    }

  \]

}

---

## Cognitive and Scientific Justification

| PFC Agent | Reference |
| :---- | :---- |
| DLPFC | Miller, E. K., & Cohen, J. D. (2001). *An integrative theory of prefrontal cortex function*. Annual Review of Neuroscience, 24, 167–202. [https://doi.org/10.1146/annurev.neuro.24.1.167](https://doi.org/10.1146/annurev.neuro.24.1.167) |
| VMPFC | Damasio, A. R. (1994). *Descartes' Error: Emotion, Reason, and the Human Brain*. Putnam. |
| OFC | Bechara, A., Damasio, H., & Damasio, A. R. (2000). *Emotion, decision making and the orbitofrontal cortex*. Cerebral Cortex, 10(3), 295–307. [https://doi.org/10.1093/cercor/10.3.295](https://doi.org/10.1093/cercor/10.3.295) |
| ACC | Amodio, D. M., & Frith, C. D. (2006). *Meeting of minds: The medial frontal cortex and social cognition*. Nature Reviews Neuroscience, 7(4), 268–277. [https://doi.org/10.1038/nrn1884](https://doi.org/10.1038/nrn1884) |
| MPFC | Samsonovich, A. V. (2010). *Toward a unified catalog of implemented cognitive architectures*. In Proceedings of the BICA Conference. |

---

## Generation Guidelines

- Generate 5–10 examples per run  
- Choose one PFC agent per batch  
- Stay within JSONL format  
- Ground assistant responses in neuroscience-based cognitive modeling  
- Use real-world complexity (social, emotional, multi-task, ethical contexts)  
- Match tone and structure to dataset style (e.g., Taskmaster vs EmpatheticDialogues)

---

## Summary

This prompt enables synthetic data generation for training LLMs to simulate the cognitive functions of PFC subregions in SCAN. Each entry:

- Represents a specialized PFC agent  
- Adheres to JSONL formatting standards  
- Aligns with neuroscience and real-world user behavior  
- Can be scaled for fine-tuning or multi-agent orchestration
