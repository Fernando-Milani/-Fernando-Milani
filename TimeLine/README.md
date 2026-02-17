# (Timeline Project)

É um projeto experimental que propõe uma **linha do tempo navegável da história humana**, estruturada em períodos e eventos interconectados, permitindo exploração progressiva por zoom temporal, similar ao conceito do Google Maps aplicado ao tempo.

O foco inicial do projeto é **arquitetura de dados, consistência e escalabilidade**, antes de qualquer preocupação com design visual.

---

## 🎯 Objetivo

Criar uma base de dados histórica estruturada que permita:

- Navegar do macro para o micro (eras → períodos → eventos)
- Associar eventos a múltiplos períodos
- Validar consistência temporal automaticamente
- Escalar para milhares ou milhões de eventos
- Servir como base para uma timeline interativa web no futuro

---

## 🧠 Conceito de Modelagem

- **Eventos** são entidades atômicas, com data absoluta e metadados.
- **Períodos** são agrupadores temporais que podem conter:
  - Outros períodos
  - Eventos
- Um evento pode pertencer a múltiplos períodos sem duplicação.
- A timeline é pensada como um **grafo temporal**, não como uma lista linear simples.

---

## 📁 Estrutura do Projeto

---

## Dependências
- -m pip install InquirerPy
- python -m http.server


### Funções e correções pendentes
- Eventos podem aceitar data completa (Dia, mês e ano), ou somente o ano
- Datas imprecisas (Adicionar data central e margem de erro)
- Destaque e seleção TL <-> Card
- Favoritar
- Filtro de cards (ordenar por nome, data, etc)
- Modificar verificação de datas em eventos
- Estilização

### Funções e correções feitas
- Transformar anos negativo em a.C. (-2500 -> 2500 a.C.)
- Editar eventos e períodos pelo manager
- Quando um evento for apagado, apagar também as referências a ele nos períodos
- LoD na TL
- Medições na TL (Min, mid, max, mouse pointer)



<article>
  <h1></h1>

  <img src="" alt="">

  <p>
    
  </p>
</article>