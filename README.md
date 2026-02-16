# Compiler Phases Implementation in Python

This repository contains a simple implementation of all six phases of a compiler using the Python programming language.

The project demonstrates how each phase of a compiler works internally. All components are implemented manually in Python for educational purposes.

---

## Compiler Phases Covered

- Lexical Analyzer  
- Syntax Analyzer  
- Semantic Analyzer  
- Intermediate Code Generation  
- Code Optimization  
- Code Generation  

Each phase is implemented separately in Python to clearly demonstrate its functionality.

---

## Project Description

This project processes source code step by step through all compiler phases:

1. **Lexical Analysis**
   - Converts source code into tokens
   - Identifies keywords, identifiers, operators, constants, and separators

2. **Syntax Analysis**
   - Validates the structure of the program using grammar rules
   - Generates a parse tree or structured representation

3. **Semantic Analysis**
   - Checks for semantic errors such as undeclared variables and type mismatches
   - Uses a symbol table for validation

4. **Intermediate Code Generation**
   - Converts validated code into intermediate representation (Three Address Code)

5. **Code Optimization**
   - Improves intermediate code efficiency
   - Performs optimizations like constant folding and dead code elimination

6. **Code Generation**
   - Produces target-level code (assembly-like representation)

---

## Technologies Used

- Python 3
- Visual Studio Code (VS Code)

---

## Structure
compiler-phases-python/
│
├── phase1_lexical_analyzer/
├── phase2_syntax_analyzer/
├── phase3_semantic_analyzer/
├── phase4_intermediate_code/
├── phase5_code_optimizer/
├── phase6_code_generator/
└── README.md
