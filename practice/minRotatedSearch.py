#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> solution(string text, int width) {
    // Storing all the sentences
    vector<string> s;
    string sentence = "";

    for (char ch : text) {
        sentence += ch;

        // Sentence ending
        if (ch == '.' || ch == '?' || ch == '!') {
            s.push_back(sentence);
            sentence = "";
        }
    }

    // Preparing the final result array
    vector<string> ans;

    // Initial * array
    string init;
    for (int i = 0; i < width + 2; i++) {
        init += '*';
    }

    ans.push_back(init);

    for (string st : s) {
        // st is the sentence that we are processing
        string line = "";
        for (char ch : st) {
            if (line.length() == width - 3) {
                ans.push_back("*" + line + " *");
                line = "";
            }
            line += ch;
        }

        // Add the last line of the sentence
        ans.push_back("*" + line + string(width - line.length() - 2, ' ') + " *");
    }

    // Add the bottom border
    ans.push_back(init);

    return ans;
}

int main() {
    string text = "Hi! This is the article you have to format properly. Could you do that for me, please?";
    int width = 16;

    vector<string> result = solution(text, width);

    for (string line : result) {
        cout << line << endl;
    }

    return 0;
}
