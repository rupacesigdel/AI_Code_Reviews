document.addEventListener("DOMContentLoaded", () => {
    const analyzeButton = document.getElementById("analyzeButton");
    const submitFeedbackButton = document.getElementById("submitFeedbackButton");
    const analysisResult = document.getElementById("analysisResult");
    const resultDisplay = document.getElementById("resultDisplay");
    const feedbackInput = document.getElementById("feedbackInput");

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    analyzeButton.addEventListener("click", async () => {
        const codeInput = document.getElementById("codeInput").value;

        if (!codeInput) {
            alert("Please paste your code before analyzing.");
            return;
        }

        try {
            const response = await fetch("/analyze-code/", { 
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                },
                body: JSON.stringify({ code: codeInput })
            });

            if (!response.ok) throw new Error("Failed to analyze code");

            const data = await response.json();
            console.log("Response data:", data);
            if (data.result) {
                resultDisplay.textContent = data.result;
                analysisResult.classList.remove("hidden");
            } else {
                console.error("No result in response:", data);
                alert("No result returned from backend.");
            }
            
        } catch (error) {
            alert(`Error: ${error.message}`);
        }
    });

    submitFeedbackButton.addEventListener("click", async () => {
        const feedback = feedbackInput.value;

        if (!feedback) {
            alert("Please provide feedback before submitting.");
            return;
        }

        try {
            const response = await fetch("/submit-feedback/", { 
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                },
                body: JSON.stringify({ feedback: feedback })
            });

            if (!response.ok) throw new Error("Failed to submit feedback");

            const data = await response.json();
            alert(data.message); 
            feedbackInput.value = ""; 
        } catch (error) {
            alert(`Error: ${error.message}`);
        }
    });
});
