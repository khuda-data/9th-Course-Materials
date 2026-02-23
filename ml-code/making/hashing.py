import pandas as pd
import hashlib

# answer dictionary
answers = {
    # number : answer (string type)
    1 : "5",
    2 : "58",
    3 : "4.296828314241623",
    4 : "123"
}


def md5_norm (x) -> str :
    s = str(x).strip().lower()
    return hashlib.md5(s.encode("utf-8")).hexdigest()

answer_df = pd.DataFrame({
    "task" : list(answers.keys()),
    "answer" : [md5_norm(answers[i]) for i in answers.keys()],
})

answer_df.to_csv("answer.csv", index = False)