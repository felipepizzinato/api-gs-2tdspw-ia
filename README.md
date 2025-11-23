### API de Predição – Probabilidade de Mudança de Carreira

## 1. Visão Geral

Esta API expõe o modelo de Machine Learning desenvolvido para estimar a probabilidade de um indivíduo mudar de carreira, com base em seis variáveis explicativas selecionadas a partir de análise estatística e regras de negócio.

A API foi implementada em Flask e está hospedada na plataforma Render, permitindo o consumo pela aplicação backend e por outras integrações.

## 2. URL Base

https://api-gs-2tdspw-ia.onrender.com

## 3. Endpoints Disponíveis

### 3.1. GET /

**Descrição:**  
Endpoint de health-check simples, utilizado para verificar se a API está ativa.

**Requisição:**  
Método: GET  
URL: https://api-gs-2tdspw-ia.onrender.com/

**Resposta (200 – OK):**  
API de probabilidade de mudança de carreira está no ar

### 3.2. POST /predict

**Descrição:**  
Endpoint principal da API. Recebe os atributos de um indivíduo e retorna:

- a probabilidade estimada de mudança de carreira;
- a classe prevista (0 = não muda, 1 = muda).

**Requisição:**  
Método: POST  
URL: https://api-gs-2tdspw-ia.onrender.com/predict

**Header obrigatório:**  
Content-Type: application/json

**Corpo (JSON) com os 6 campos obrigatórios:**

| Campo | Tipo | Descrição |
|-------|------|-----------|
| Job Satisfaction | int | Nível de satisfação no trabalho atual (1 a 10). |
| Salary | float/int | Salário atual. |
| Field of Study (Class) | int | Código numérico da área de formação. |
| Current Occupation (Class) | int | Código numérico da ocupação atual. |
| Education Level (Class) | int | Código numérico do nível educacional. |
| Age | int | Idade do indivíduo. |

**Importante:**  
Os valores devem ser enviados já codificados conforme a base de treinamento.

**Exemplo de corpo da requisição:**

```json
{
  "Job Satisfaction": 9,
  "Salary": 20000,
  "Field of Study (Class)": 3,
  "Current Occupation (Class)": 2,
  "Education Level (Class)": 4,
  "Age": 30
}
```

shell
Sempre exibir os detalhes

Copiar código

## 4. Formato da Resposta

### 4.1. Resposta de sucesso (200 – OK)

{
"classe_prevista": 1,
"probabilidade_mudar": 0.8233333333333334
}

makefile
Sempre exibir os detalhes

Copiar código

### Campos:

| Campo | Tipo | Descrição |
|--------|-------|-----------|
| classe_prevista | int | 0 = não muda, 1 = muda de carreira |
| probabilidade_mudar | float | Valor entre 0 e 1 |

Cutoff:  
classe_prevista = 1 se probabilidade_mudar ≥ 0.5  
classe_prevista = 0 se probabilidade_mudar < 0.5

### 4.2. Respostas de erro

**a) JSON ausente ou inválido (400 – Bad Request)**

{
"error": "JSON não recebido ou Content-Type incorreto. Envie 'Content-Type: application/json'.",
"expected_fields": [
"Job Satisfaction",
"Salary",
"Field of Study (Class)",
"Current Occupation (Class)",
"Education Level (Class)",
"Age"
]
}

css
Sempre exibir os detalhes

Copiar código

**b) Campos obrigatórios faltando (400 – Bad Request)**

{
"error": "Campos faltando no JSON",
"expected_fields": [
"Job Satisfaction",
"Salary",
"Field of Study (Class)",
"Current Occupation (Class)",
"Education Level (Class)",
"Age"
],
"missing_fields": [
"Age"
]
}

shell
Sempre exibir os detalhes

Copiar código

## 5. Exemplo de Consumo

### 5.1. Via curl

curl -X POST https://api-gs-2tdspw-ia.onrender.com/predict
-H "Content-Type: application/json"
-d '{
"Job Satisfaction": 8,
"Salary": 50000,
"Field of Study (Class)": 3,
"Current Occupation (Class)": 1,
"Education Level (Class)": 2,
"Age": 25
}'

shell
Sempre exibir os detalhes

Copiar código

### 5.2. Via JavaScript (fetch)

fetch("https://api-gs-2tdspw-ia.onrender.com/predict", {
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify({
"Job Satisfaction": 8,
"Salary": 50000,
"Field of Study (Class)": 3,
"Current Occupation (Class)": 1,
"Education Level (Class)": 2,
"Age": 25
})
})
.then(res => res.json())
.then(data => {
console.log("Classe prevista:", data.classe_prevista);
console.log("Probabilidade de mudar:", data.probabilidade_mudar);
})
.catch(err => console.error(err));
