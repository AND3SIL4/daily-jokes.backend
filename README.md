# Daily jokes project

## Architecture

LAYERED ARCHITECTURE

```txt
app/
├── api/
│   ├── _init_.py
│   └── endpoints/
│       ├── _init_.py
│       └── jokes.py        # Endpoints relacionados con los chistes
├── core/
│   ├── _init_.py
│   └── config.py           # Configuración global (p. ej., variables de entorno, settings)
├── db/
│   ├── _init_.py
│   ├── models.py           # Modelos de base de datos (puedes usar SQLAlchemy o sqlite3 según el caso)
│   └── session.py          # Manejo de la conexión y sesión con la base de datos
├── schemas/
│   ├── _init_.py
│   └── joke.py             # Esquemas Pydantic para validación y serialización
└── main.py                 # Punto de entrada de la aplicación
```

---

_developed by `felipe-silva`_
