# DUTIR BioNLP Schema Documentation
Based on [BigBio project](https://github.com/bigscience-workshop/biomedical), we have defined a set of lightweight, task-specific schema to help simplify programmatic access to common biomedical datasets. This schema should be implemented for each dataset in addition to a schema that preserves the original dataset format.

## Content
- [DUTIR BioNLP Schema Documentation](#dutir-bionlp-schema-documentation)
  - [Content](#content)
  - [Information Extraction (IE)](#information-extraction-ie)
    - [Passages](#passages)
    - [Entities (NER/NEN)](#entities-nernen)
    - [Relations (RE)](#relations-re)
    - [Causal (CRE)](#causal-cre)
    - [Event (EE)](#event-ee)
    - [Coreference resolution (COREF)](#coreference-resolution-coref)
  - [Text Classification (TC)](#text-classification-tc)
  - [Question Answering (QA)](#question-answering-qa)
    - [Multiple Choice (multiple\_choice)](#multiple-choice-multiple_choice)
    - [Simple Answer Questions (sqa)](#simple-answer-questions-sqa)
    - [Context-based Answer Questions (cqa)](#context-based-answer-questions-cqa)
  - [Multi-Round Dialogue (MRD)](#multi-round-dialogue-mrd)
  - [Machine Translation (MT)](#machine-translation-mt)
  - [Text Pairs (TP)](#text-pairs-tp)
    - [Textual Entailment (te)](#textual-entailment-te)
    - [Semantic Similarity (ss)](#semantic-similarity-ss)
  - [Text to Text/Struct (TT)](#text-to-textstruct-tt)
    - [Document Summarization (ds)](#document-summarization-ds)
    - [Text to Struct (ts)](#text-to-struct-ts)

## Information Extraction (IE)

This is a simple container format with minimal nesting that supports a range of information extraction tasks:

- Named entity recognition (NER) (**Example: Chinese/CMeEE-V2**) and Named entity normalization/linking (NEN)  (**Example:English/ncbi_disease**)
- Relation extraction (RE) (**Example: Chinese/CMeIE-V2**)
- Causal relation extraction （CRE）
- Event extraction (EE) 
- Coreference resolution (COREF)

```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "passages": [...],
    "entities": [...],
    "events": [...],
    "coreferences": [...],
    "relations": [...],
}
```



**Schema Notes**

- `id` fields appear at the top (i.e. document) level. They start with "0" that makes every `id` field in a dataset unique.
- `document_id` should be a dataset provided document id. If not provided in the dataset, it can be set equal to the top level `id`.
- `passages` captures document structure such as named sections. It can be empty fields if no document strcture.
- `entities`, `events`, `coreferences`, `relations` may be empty fields depending on the dataset and specific task.



### Passages

Passages capture document structure, e.g., the title and abstact sections of a document.  `Passages` can be empty fields if no document strcture.
- `offsets` contain character offsets into the string that would be created from `" ".join([passage["text"] for passage in passages])`
- `offsets` and `text` are always lists to support discontinous spans. For continuous spans, they will have the form `offsets=[(lo,hi)], text=["text span"]`. For discontinuous spans, they will have the form `offsets=[(lo1,hi1), (lo2,hi2), ...], text=["text span 1", "text span 2", ...]`


```
{
    "id": "0",
    "document_id": "227508",
    "passages": [
        {
            "id": "0",
            "type": "title",
            "text": ["Naloxone reverses the antihypertensive effect of clonidine."],
            "offsets": [[0, 59]]
        },
        {
            "id": "1",
            "type": "abstract",
            "text": ["In unanesthetized, spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine, 5 to 20 micrograms/kg, was inhibited or reversed by nalozone, 0.2 to 2 mg/kg. The hypotensive effect of 100 mg/kg alpha-methyldopa was also partially reversed by naloxone. Naloxone alone did not affect either blood pressure or heart rate. In brain membranes from spontaneously hypertensive rats clonidine, 10(-8) to 10(-5) M, did not influence stereoselective binding of [3H]-naloxone (8 nM), and naloxone, 10(-8) to 10(-4) M, did not influence clonidine-suppressible binding of [3H]-dihydroergocryptine (1 nM). These findings indicate that in spontaneously hypertensive rats the effects of central alpha-adrenoceptor stimulation involve activation of opiate receptors. As naloxone and clonidine do not appear to interact with the same receptor site, the observed functional antagonism suggests the release of an endogenous opiate by clonidine or alpha-methyldopa and the possible role of the opiate in the central control of sympathetic tone."],
            "offsets": [[60, 1075]]
        },
    ],
}
```

### Entities (NER/NEN)
- `normalized` sub-component may contain 1 or more normalized links to database entity identifiers. Here, "db_name" denotes the database name, "db_id" denotes the entity indentifier in this database.

```
"entities": [
    {
        "id": "0",  
        "offsets": [[0, 8]],
        "text": ["Naloxone"],
        "type": "Chemical",
        "normalized": [{"db_name": "MESH", "db_id": "D009270"}]
    },
    ...
 ],
```


### Relations (RE)
- `type` is the relation type. 
- `arg1_id` is the first entity identifier of the relation. 
- `arg2_id` is the second entity identifier of the relation. 

```
"relations": [
    {
        "id": "0",
        "type": "chemical-induced disease",
        "arg1_id": "10",
        "arg2_id": "32"
    }
]
```

### Causal (CRE)
- `type` is the relation type. 
- `arg1` is the first entity identifier of the relation. It can be an entity (the arg 1 "type" should be set to "entity") or a relation (the arg2 "type" should be set to "relation").
- `arg2` is the second entity identifier of the relation. It can be an entity (the arg 1 "type" should be set to "entity") or a relation (the arg2 "type" should be set to "relation").

```
"causal": [
    {
        "id": "0",
        "type": "条件关系",
        "arg1": {"id":"3", "type":"entity"},
        "arg2": {"id":"0", "type":"relation"}
    }
]
```

### Event (EE)

```
"events": [
    {
        "id": "0",
        "type": "Reaction",
        "trigger": {
            "offsets": [[0,6]],
            "text": ["reacts"]
        },
        "arguments": [
            {
                "role": "Theme",
                "ref_id": "5",
                "text": "corpus luteum"
            },
            {
                "role": "Instrument", # if the argument is not entity, set "ref_id" to "", only provide the text.
                "ref_id": ""
                "text": "...."
            }
        ]
    }
]

```

### Coreference resolution (COREF)
- `entity_ids` denotes the several entity names refer to the same actual entity.
```
"coreferences": [
	{
	   "id": "0",
	   "entity_ids": ["1", "10", "23"],
	},
	...
]
```

## Text Classification (TC)
This is a simple container format with minimal nesting that supports a range of text classification tasks. (**Example file: Chinese/TCM-SD-TC**)

```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "text": "xxxxx",
    "labels": [...]
}
```
**Schema Notes**

- `labels` is the label of the text type.



Example:
```
{
    "id": "0",
    "document_id": "32653511",
    "text": "Potential benefits and risks of omega-3 fatty acids supplementation to patients with COVID-19.",
    "labels": ["Treatment"],
}
```

## Question Answering (QA)

This is a simple container format with minimal nesting that supports a range of question answering tasks. 


```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "question_id": "xxxxx"
    "question": "...",
    "type": "...",
    "choices": [...],
    "context": "...",
    "answer": [...],
    "long_answer": [...]
}
```

**Schema Notes**

- `id` fields appear at the top (i.e. document) level. They start with "0" that makes every `id` field in a dataset unique.
- `document_id` should be a dataset provided document id. If not provided in the dataset, it can be set equal to the top level `id`.
- `question_id` should be a dataset provided question id. If not provided in the dataset, it can be set equal to the upper level `document_id`.
- `question` should be the question input. Some datasets' questions and  contexts may be independent, please put the contexts into `context` field.
- `type` can be "yesno", "multiple_choice" or "dialogue".
- `choices` whould be provided when the dataset type is "yesno" or "multiple_choice".
- `answer` should be the answer output. Some "yesno" and "multiple_choice" datasets may provide addtional long answers to explain the choice, please put them into '`long_answer`' field.
- `context`, `long_answer` may be empty fields depending on the dataset and specific task.


### Multiple Choice (multiple_choice)
(**Example file: English/med_qa**)
```
{
    "id": "0",
    "question_id": "0",
    "document_id": "0",
    "question": "A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus. Which of the following is the best treatment for this patient?",
    "type": "multiple_choice",
    "choices": ["Ampicillin", "Ceftriaxone", "Ciprofloxacin", "Doxycycline", "Nitrofurantoin"],
    "context": "",
    "answer": ["Nitrofurantoin"],
    "long_answer": []
}
```
### Simple Answer Questions (sqa)
(**Example file: Chinese/BenTsao_livercacer**)
```
{
    "id": "2",
    "question_id": "2",
    "document_id": "2",
    "question": "Hello doctor,I just got one side of my wisdom teeth removed both upper and lower six days ago, and I have another one scheduled after two days for the left side. The upper is 100 % fine, which they pulled. The lower they pulled the tooth without removing the root because it was too close to the nerve. I do have some stitching in this area currently on the lower cheek. Noticed a hard lump about 1 inch between my lower jawline and cheek area. Is this normal because of swelling or something else. Currently taking Amoxicillin 500 mg and Ibuprofen 600 mg. Please let me know what this hard lump is, also generally on the lower side where this lump is, remains sore.",
    "type": "sqa",
    "choices": [],
    "context": "",
    "answer": ["Hello. The lump is mostly a hard swelling which forms postsurgical removal of the wisdom tooth or maybe even by swollen lymph nodes due to infection. It takes a week or two for the swelling to subside. Sometimes, if the root is still inside, the infection may be remaining there causing swelling. Get an X-ray done to find out the exact problem and stronger antibiotics like Augmentin (Amoxicillin and Clavulanic acid) along with a painkiller for a week."],
    "long_answer": []
    }
```

### Context-based Answer Questions (cqa)
(**Example file: Chinese/TCM_Literature_QA**)

```
{
    "id": "0",
    "document_id": "828",
    "question_id": "0",
    "question": "“干呕、吐涎沫、头痛者吴茱萸汤主之”这句话曾出现在哪本医学巨著中？",
    "type": "cqa",
    "choices": [],
    "context": "反佐配伍的典范，始见于张仲景《伤寒杂病论》，其中记载“干呕、吐涎沫、头痛者吴茱萸汤主之”。患者病机为肝寒犯胃，浊气上逆所致头痛。胃阳不布产生涎沫随浊气上逆而吐出，肝脉与督脉交会于巅顶，肝经寒邪，循经上冲则头痛，以吴茱萸汤主治。可在吴茱萸汤中加入少许黄连反佐，用以防止方中吴茱萸、人参、干姜等品辛热太过，从而达到温降肝胃、泄浊通阳而止头痛的功效。后代医者多在清热剂和温里剂中运用此法。",
    "answer": "《伤寒杂病论》",
    "long_answer": []
}
```

## Multi-Round Dialogue (MRD)
This is a simple container format with minimal nesting that supports a range of multi-round dialogue tasks. (**Example file: Chinese/MedDialog**)
```
{
    "id": "ABCDEFG",
    "conversation_id": "XXXXXX",
    "num_turns": int,
    "context": "...",
    "chat": [...],
}
```

**Schema Notes**

- `id` fields appear at the top (i.e. document) level. They start with "0" that makes every `id` field in a dataset unique.
- `conversation_id` should be a dataset provided conversation id. If not provided in the dataset, it can be set equal to the top level `id`.
- `num_turns` is the total number of the rounds in the chat.
- `chat` should be chat context for each round.
- `context` may be empty fields depending on the dataset and specific task.

```
{
    "id": "159",
    "conversation_id": "159",
    "num_turns": 2,
    "context": "",
    "chat": [
        {
            "patient": "hello doctor, i get a cough for the last few days, which is heavy during night times. no raise in temperature but feeling tired with no travel history. no contact with any covid-19 persons. it has been four to five days and has drunk a lot of benadryl and took paracetamol too. doctors have shut the op so do not know what to do? please help.",
            "doctor": "hello, i understand your concern. i just have a few more questions. does your cough has phlegm? any other symptoms like difficulty breathing? any other medical condition such as asthma, hypertension? are you a smoker? alcoholic beverage drinker?"
        },
        {
            "patient": "thank you doctor, i have phlegm but not a lot. a tiny amount comes out most of the time. i have no difficulty in breathing. no medical conditions and not a smoker nor a drinker.",
            "doctor": "hi, i would recommend you take n-acetylcysteine 200 mg powder dissolved in water three times a day. you may also nebulize using pnss (saline nebulizer) three times a day. this will help the phlegm to come out. i would also recommend you take vitamin c 500 mg and zinc to boost your immune system. if symptoms persist, worsen or new onset of symptoms has been noted, further consult is advised."
        }
    ]
}
```

## Machine Translation (MT)
This is a simple container format with minimal nesting that supports a range of machine translation tasks. (**Example file: English/paramed**)
```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "multilingual": [...]
}
```



**Schema Notes**

- `multilingual` sub-component may contain two or more normalized parallel texts.
- `language` is the languge of this text. "zh" denotes Chinese, "en" denotes English.


```
{
	"id": "0",
	"document_id": "0",
	"multilingual": [
        {
            "id": "0",  
            "text": "也许不能: 分析结果提示激素疗法在维持去脂体重方面作用很小。",
            "language": "zh",
        },
        {
            "id": "1",  
            "text": "probably not: analysis suggests minimal effect of HT in maintaining lean body mass.",
            "language": "en",
        }
    ]
}
```




## Text Pairs (TP)

This is a simple container format with minimal nesting that supports a range of text pairs tasks. 


```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "text_1": "...",
    "text_2": "...",
    "label": [...]
}
```

**Schema Notes**

- `id` fields appear at the top (i.e. document) level. They start with "0" that makes every `id` field in a dataset unique.
- `document_id` should be a dataset provided document id. If not provided in the dataset, it can be set equal to the top level `id`.
- `text_1` is the first text.
- `text_2` is the second text.
- `label` is the label of Text Pairs.



### Textual Entailment (te)

```
{
	"id": "0",
	"document_id": "0",
	"text_1": "Pluto rotates once on its axis every 6.39 Earth days;",
	"text_2": "Earth rotates on its axis once times in one day.",
	"label": "neutral"
}
```
**Schema Notes**

- `text_1` is the premise.
- `text_2` is the hypothesis.

### Semantic Similarity (ss)

```
{
  "id": "0",
  "document_id": "0",
  "text_1": "Am I over weight (192.9) for my age (39)?",
  "text_2": "I am a 39 y/o male currently weighing about 193 lbs. Do you think I am overweight?",
  "label": "1"
}
```

**Schema Notes**

- `label` is the label of the semantic similarity between the texts are the same. 

## Text to Text/Struct (TT)
This is a simple container format with minimal nesting that supports a range of text generation tasks. 
- Text Summarization 
- Text to Struct 


```
{
    "id": "ABCDEFG",
    "document_id": "XXXXXX",
    "type": "...",
    "input": "...",
    "output": [...],
}
```
- `type` can be "txt2txt" or "txt2struct".
### Document Summarization (ds)
```
{
  "id": "0",
  "document_id": "1-131188152",
  "type": "txt2txt",
  "input": "SUBJECT: who and where to get cetirizine - D\nMESSAGE: I need/want to know who manufscturs Cetirizine. My Walmart is looking for a new supply and are not getting the recent",
  "output": ["Who manufactures cetirizine?"],
}
```
**Schema Notes**

- `input` is the original text.
- `output` is the summarization.

### Text to Struct (ts)
```
{
  "id": "0",
  "document_id": "10301581",
  "type": "txt2struct",
  "input": "医生:你好，咳嗽是连声咳吗？有痰吗？有没流鼻涕，鼻塞？\n医生: 咳嗽有几天了？\n患者: 有三天\n......",
  "output": [{
                "主诉": "晚上咳嗽，磨牙。",
                "现病史": "患儿夜间咳嗽三天，磨牙，大便干。未服用药物。",
                "辅助检查": "暂缺。",
                "既往史": "不详。",
                "诊断": "消化不良。",
                "建议": "小儿消积止咳口服液，益生菌，到医院化验血常规。"
            }],
}
```
**Schema Notes**

- `input` is the input text.
- `output` is the struct output.





