# Notes for Dev

- `python -m venv .bco_env`

- `. .bco_env/bin/activate`

- Class BCO
	Atributes:
	- ID
	- Schema
	- Extensions?
	- ErrorDomian?
	- Status(valid or such)
	- pubStatus?
	- etag
	Methods:
	- validate
	- verify
	- etag check
	- etag generation

### TODOs ...
- enable `critical` errors and `warnings`
	- incomplete or unresolvable schema should be a warning
- enable check for empty fields. 
