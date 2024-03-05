export class GradeSchool {
  private studentRoster: { [key: number]: string[] };

  constructor() {
    this.studentRoster = {};
  }

  /**
   * Returns a deep copy of the roster.
   */
  roster() {
    return JSON.parse(JSON.stringify(this.studentRoster));
  }

  /**
   * Moves the student into a different grade in the roster.
   */
  private update(name: string) {
    for (const [grade, students] of Object.entries(this.studentRoster)) {
      if (students.includes(name)) {
        this.studentRoster[parseInt(grade)] = students.filter(
          (student) => student !== name
        );
      }
    }
  }

  /**
   * Adds a new student to the roster.
   */
  add(name: string, grade: number) {
    this.update(name);

    if (this.studentRoster[grade]) {
      this.studentRoster[grade].push(name);
      this.studentRoster[grade].sort();
    } else this.studentRoster[grade] = [name];
  }

  /**
   * Returns a deep copy of a grade from the roster.
   */
  grade(grade: number): string[] {
    return this.studentRoster[grade]
      ? JSON.parse(JSON.stringify(this.studentRoster[grade]))
      : [];
  }
}
