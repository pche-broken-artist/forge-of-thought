---
project: forge
title: User stories — vrstva uživatelských příběhů pod BRD
author: FT-
version: 0.5
status: draft
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

## Co chci
Vrstvu řetězu pro user stories, `35-user-stories.md`, mezi BRD a
solution designem, pracovanou přes `/forge user-stories`.

## Proč
User stories popisují funkcionalitu z pohledu uživatele, ne jako
technické zadání. Drží hodnotu — co, pro koho a proč — a člení práci
na části, které lze vyvinout a otestovat. Schvalují je stakeholdeři
jako celek; po schválení je přebírá vývoj, dělá nad nimi technickou
analýzu a vyvíjí podle nich, pokud nezůstávají prázdná místa; testeři
z nich píšou test cases. Výstupem analytika je dokument se seznamem
stories, nejčastěji v Confluence.

## Z čeho vychází
Z požadavků jakéhokoli druhu (BR, NFR, bezpečnostní a další), vazba
mnoho na mnoho: z jednoho BR může být více stories a jedna story může
pokrývat více BR. U malé změny, kde je zadání přesné a bez dalších
dopadů, přímo z intentu; zda zadání stačí, rozhoduje analytik.

## Tvar story
- Story je jedna funkce, jak ji potkává ten, kdo ji používá. Varianty
  podle podmínek, kvality a přechody jsou její akceptační kritéria a
  edge cases, ne samostatné stories; nová story začíná u jiného
  aktéra nebo jiné funkce. Běžné chování je kritérium, edge case je
  hraniční situace.
- ID `US.NNNN`, číslované po desítkách, skupiny po stovkách; název
  jako krátké podstatné jméno funkce.
- Pořadí oddílů: název; volná věta nesoucí kdo nebo co, co a proč
  (šablona „Jako… chci… abych…“ se nevyžaduje ani nezakazuje);
  akceptační kritéria v odrážkách; `Edge cases` (situace → co se
  stane); `Risks`, vždy s mitigací nebo důsledky; `Note`, jen odkaz
  na přílohu či technickou analýzu s vysvětlením, co se za ním
  skrývá; `Questions` (otázka → vlastník); `Reference` (BR, NFR,
  DEP… nebo POS).
- Povinná je jen `Reference`; ostatní oddíly se vynechávají, když
  story nic nemá. Export pro stakeholdery odkazy na POS vynechává,
  protože intent nevidí; story jen s POS v exportu řádek Reference
  nemá.
- Popisky oddílů anglicky a pevně, obsah v jazyce projektu.
- Nefunkční požadavky: průřezové jako samostatná story, týkající se
  jedné funkce jako akceptační kritérium u ní.
- Dokument nese jen stories.

## Formulace
Akceptační kritéria v oznamovacím způsobu přítomného času, jedno
chování na odrážku. Žádná vágní slova („rychle“, „vhodně“,
„intuitivně“); chybí-li hodnota, zapíše se otevřená otázka. Bez
technického řešení — komponenty, API, datového modelu —, nanejvýš
odkaz na přílohu nebo technickou analýzu.

## Kdy jsou hotové
- Každý požadavek je pokrytý alespoň jednou story, nebo je řečeno,
  proč ne.
- Každé akceptační kritérium je testovatelné.
- Stories si neodporují a stejná funkce není popsaná dvakrát jinak.
- Každá otevřená otázka má vlastníka; story s otázkou, která blokuje
  vývoj, není hotová.
- Stories jako celek schválili stakeholdeři.

## Jak vznikají
Claude nejdřív navrhne řez: názvy stories s krátkým popisem a
požadavky, které žádná story nepokryje, popsané slovy. Až ho analytik
schválí, rozepíše celé stories z BRD (u malé změny z intentu) a
analytik je projde story po story. Kde zadání nestačí,
přepne se na rozhovor nad jednotlivou story. Co chybí, se nedomýšlí:
zapíše se otevřená otázka.

## Kontrola a výstup
- Nová mechanická kontrola `check-user-stories` po vzoru `check-brd`:
  pokrytí požadavků, existující citovaná ID, kritéria a edge cases,
  otázky s vlastníkem, rizika s mitigací nebo důsledky, Note s odkazem
  a vysvětlením.
- Kritik `clarity` zná styl stories a nehlásí jeho odlišnost od stylu
  požadavků.
- Render podle receptu vyrobí přesně formát exportu
  (`sources/example-user-stories-v2.md`): pevné nadpisy a věta o
  účelu, bez tabulky, nadpis na story, části na samostatných řádcích,
  bez zalamování, aby šel vložit do Confluence i Jiry.

## Co nechci
Prioritu, odhad, technické řešení, detail grafiky, rozpad na úkoly,
oddíl poznámek, samostatný oddíl závislostí (závislost je `DEP`
v Reference, u malé změny otevřená otázka), úvod nebo předpoklady
v dokumentu.

## Změna enginu navíc
Prefix ID o dvou nebo třech písmenech (POS.0220, ID schéma v
`CLAUDE.md`) a výraz `[A-Z]{2,3}` ve skriptech, aby fungovala `US`,
`BR` i `UC`. Pravidlo o třech písmenech vychází ze souladu se
skupinovým standardem BRD (REJ.0100) a engine ho porušil už u `BR` a
`UC` (POS.1830).

## Postup
Podle POS.1780: tento brief, pak definice se šablonou, kontrola a
recept, pak zkouška na malém projektu (zadání: vazba obsahu v CMS
na úroveň hráče), teprve potom pozice v intentu enginu a
položka solution designu.
