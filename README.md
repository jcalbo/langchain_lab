# langchain_lab

Some basic examples and exercises to practice langchain artifacts and methods.

Updated with the new version of Langchain 0.2.6 that requires 
to install  ```langchain-openai``` and then import ChatOpenAI
```
from langchain_openai import ChatOpenAI
```

Also, I've updated the method to invoke the chain which changed to:

```python
    chain = prompt_template | llm
```
