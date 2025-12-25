from processing.store import VectorStore

store = VectorStore()
count = store.count()
print(f"Total Documents in DB: {count}")

if count > 0:
    print("Sample Data:")
    peek = store.peek(1)
    print(peek)
else:
    print("Database is empty.")
