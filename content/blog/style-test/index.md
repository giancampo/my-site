---
title: "Style test: titoli, tabelle, codice, math, icone"
date: 2026-11-01
draft: true
tags: ["analytics"]
---

Pagina di prova (draft, non viene pubblicata) per verificare la resa di tutti gli elementi.

## Titolo di sezione H2

Testo normale con **grassetto**, *corsivo* e `codice inline`. Icone: {{< icon "github" >}} {{< icon "linkedin" >}} {{< icon "check" >}}

### Sottosezione H3

| Metrica | GA4 | Universal |
|---|---:|---:|
| Sessioni | 1.240 | 1.310 |
| Utenti | 980 | 1.002 |
| Conversioni | 42 | 39 |

## Codice

```python
import pandas as pd
df = pd.read_csv("events.csv")
print(df.groupby("event_name").size())
```

## Matematica

{{< katex >}}
Inline: \(CR = \frac{conv}{sessions}\)

$$
\text{ROAS} = \frac{\sum_{i=1}^{n} revenue_i}{spend}
$$

## Immagine (click per ingrandire)

![Esempio](sample.png)

{{< alert >}}
Box di avviso con icona, utile per note e warning.
{{< /alert >}}
