# AST-Code-Analyzer
AST Code Analyzer is a sophisticated static analysis tool that employs Abstract Syntax Tree (AST) parsing to comprehensively audit Python codebases for security vulnerabilities, naming convention violations, and structural complexity. It delivers immediate, actionable feedback directly in the terminal, enforcing enterprise-grade code quality and safety standards essential for mission-critical applications such as ERP systems and medical software.

# Features
AST-Based Analysis: Understands code structure rather than just searching for text.

Security Guardrails: Detects dangerous eval() calls to prevent injection attacks.

Quality Control: Identifies poor naming conventions (short function names).

Complexity Check: Flags functions with excessive arguments to promote clean code.

# How It Works
The tool uses Python's Abstract Syntax Tree (AST) module to parse source code into a logical tree. It "visits" specific nodes—like function definitions and call expressions—comparing them against predefined safety and style rules without actually executing the code.

# How to Run
python my_tool.py app_logic.py
