export class Clock {
  private time: { [key: string]: number };

  constructor(hour: number, minute?: number) {
    let _hour = (hour % 24) + Math.floor(minute ? (minute / 60) % 24 : 0);
    let _minute = minute ? minute % 60 : 0;

    while (_hour < 0) {
      _hour = _hour + 24;
    }

    while (_minute < 0) {
      _minute = _minute + 60;
    }

    this.time = {
      hour: _hour,
      minute: _minute,
    };
  }

  public toString(): string {
    const hour =
      this.time.hour < 10 ? `0${this.time.hour}` : `${this.time.hour}`;

    const minute =
      this.time.minute < 10 ? `0${this.time.minute}` : `${this.time.minute}`;

    return hour + ":" + minute;
  }

  public plus(minutes: number): Clock {
    const _hours = Math.floor(((this.time.minute + minutes) / 60) % 24);
    this.time.hour = (this.time.hour + _hours) % 24;

    const _minutes = minutes % 60;
    this.time.minute = (this.time.minute + _minutes) % 60;

    return this;
  }

  public minus(minutes: number): Clock {
    let _hours = Math.floor(((this.time.minute - minutes) / 60) % 24);
    this.time.hour = (this.time.hour + _hours) % 24;

    const _minutes = minutes % 60;
    this.time.minute = this.time.minute - _minutes;

    this.time.hour = this.time.hour < 0 ? this.time.hour + 24 : this.time.hour;
    this.time.minute =
      this.time.minute < 0 ? this.time.minute + 60 : this.time.minute;

    return this;
  }

  public equals(other: Clock): boolean {
    return (
      this.time.hour == other.time.hour && this.time.minute == other.time.minute
    );
  }
}
