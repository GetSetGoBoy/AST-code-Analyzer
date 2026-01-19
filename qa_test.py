import rag_engine

test_cases = {
    "eval(data)": "ast.literal_eval",
    "password = '123'": "Environment Variables",
    "strcpy(a, b)": "strncpy",
    "innerHTML": "textContent"
}

def run_qa_report():
    print("--- 📝 RAG ACCURACY REPORT ---")
    passed = 0
    total = len(test_cases)

    for code, expected_keyword in test_cases.items():
        actual_advice = rag_engine.get_advice(code)
        
        if expected_keyword.lower() in actual_advice.lower():
            print(f"✅ PASS | Input: {code}")
            passed += 1
        else:
            print(f"❌ FAIL | Input: {code}")
            print(f"   Expected: {expected_keyword} | Got: {actual_advice}")

    accuracy = (passed / total) * 100
    print(f"\nTOTAL ACCURACY: {accuracy}%")
    print("------------------------------")

if __name__ == "__main__":
    run_qa_report()