## How to run

virtualenv or conda environment are recommended.

1. Make sure you have installed all the required libraries including these ones: 

```
numpy==2.0.2
torch==2.3.1+cpu
simalign>=0.4
sentencepiece>=0.2.0
apertium>=0.2.4
apertium-streamparser>=5.0.2
apertium2ud>=0.0.7
```

May work with different versions combinations, but no guarantees here.

2. Then:

```bash
cd tratreetra/example/
python example.py
python evaluation.py
```
