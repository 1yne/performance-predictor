<script>
  // @ts-nocheck
  let prev_exam_score = $state(0),
    attendance_percentage = $state(0),
    study_hours_per_day = $state(0),
    assignments_completed = $state(0),
    assignment_average = $state(0),
    quiz_average = $state(0),
    classes_missed = $state(0);

  async function click() {
    const response = await fetch("/api/run", {
      method: "POST",
      body: JSON.stringify([
        prev_exam_score,
        attendance_percentage,
        study_hours_per_day,
        assignments_completed,
        assignment_average,
        quiz_average,
        classes_missed,
      ]),
      headers: {
        "Content-Type": "application/json",
      },
    });

    const total = await response.json();
    alert(total);
  }
</script>

<div class="wrap">
  <h1 class="head">Performance Predictor</h1>
  <div class="fields">
    <div class="fields1">
      <div class="fields2">
        <h2>Previous Exam Score:</h2>
        <input type="number" bind:value={prev_exam_score} />
      </div>
      <div class="fields2">
        <h2>Attendance Percentage:</h2>
        <input type="number" bind:value={attendance_percentage} />
      </div>
    </div>
    <div class="fields1">
      <div class="fields2">
        <h2>Study Hours per Day:</h2>
        <input type="number" bind:value={study_hours_per_day} />
      </div>
      <div class="fields2">
        <h2>Assignments Completed:</h2>
        <input type="number" bind:value={assignments_completed} />
      </div>
    </div>
    <div class="fields1">
      <div class="fields2">
        <h2>Assignment Average:</h2>
        <input type="number" bind:value={assignment_average} />
      </div>
      <div class="fields2">
        <h2>Quiz Average:</h2>
        <input type="number" bind:value={quiz_average} />
      </div>
    </div>
    <div class="fields1">
      <div class="fields2">
        <h2>Classes Missed:</h2>
        <input type="number" bind:value={classes_missed} />
      </div>
    </div>
  </div>
  <button onclick={click}>Predict Next Exam Score</button>
  <!-- [78,90,3,9,80,76,3] -->
</div>

<style>
  * {
    font-family: "Montserrat";
    color: white;
  }
  .wrap {
    display: flex;
    align-items: center;
    flex-direction: column;
    gap: 2rem;
    padding: 2rem;
  }
  h1,
  h2 {
    margin: 0;
  }
  .head {
    font-size: 5rem;
    font-weight: 1000;
    color: white;
  }
  .fields {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    border: 1px solid white;
    border-radius: 1rem;
    padding: 2rem;
  }
  .fields1 {
    display: flex;
    gap: 8rem;
  }
  .fields2 {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
  input {
    padding: 0.5rem;
    border-radius: 0.5rem;
    color: black;
    border: none;
  }
  input:focus {
    /* Removes the default blue/black focus ring */
    outline: none;

    /* Adds a custom, accessible style that fits your design */
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.25);
  }
  button {
    color: black;
    font-size: 1rem;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    border: none;
    transition: background-color 0.3s, color 0.3s;
  }
  button:hover {
    background-color: #AABBE1;
    color: white;
    border: #2563eb;
  }
</style>
