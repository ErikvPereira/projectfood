console.log("JS carregado!");
document.addEventListener('DOMContentLoaded', () => {

    const ingredientsContainer =
        document.getElementById('ingredients-container');

    const stepsContainer =
        document.getElementById('steps-container');


    // ======================
    // INGREDIENTES
    // ======================

    function addIngredientRow() {

        const row = document.createElement('div');

        row.classList.add('ingredient-row');

        row.innerHTML = `
            <input
                type="text"
                name="ingredient_name[]"
                placeholder="Ingrediente"
            >

            <input
                type="text"
                name="ingredient_quantity[]"
                placeholder="Quantidade"
            >
        `;

        ingredientsContainer.appendChild(row);

        const inputs = row.querySelectorAll('input');

        inputs.forEach(input => {
            input.addEventListener(
                'input',
                checkIngredientRows
            );
        });
    }


    function checkIngredientRows() {

        const rows =
            ingredientsContainer.querySelectorAll(
                '.ingredient-row'
            );

        const lastRow = rows[rows.length - 1];

        const inputs =
            lastRow.querySelectorAll('input');

        const hasContent =
            Array.from(inputs).some(
                input => input.value.trim() !== ''
            );

        if (hasContent) {
            addIngredientRow();
        }
    }


    // ======================
    // PASSOS
    // ======================

    function addStepRow() {

        const stepNumber =
            stepsContainer.children.length + 1;

        const row = document.createElement('div');

        row.classList.add('step-row');

        row.innerHTML = `
            <label>${stepNumber}.</label>

            <textarea
                name="steps[]"
                placeholder="Descreva o passo ${stepNumber}"
                rows="2"
            ></textarea>
        `;

        stepsContainer.appendChild(row);

        const textarea =
            row.querySelector('textarea');

        textarea.addEventListener(
            'input',
            checkStepRows
        );
    }


    function checkStepRows() {

        const rows =
            stepsContainer.querySelectorAll(
                '.step-row'
            );

        const lastRow = rows[rows.length - 1];

        const textarea =
            lastRow.querySelector('textarea');

        if (
            textarea.value.trim() !== ''
        ) {
            addStepRow();
        }
    }


    // ======================
    // PRIMEIRA LINHA
    // ======================

    addIngredientRow();

    addStepRow();

});