#!/usr/bin/env python3
"""Genera una matriz sintetica de features GC-MS para las practicas."""

from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path


GROUPS = (("Good", 8), ("Bad", 8), ("Culture", 8))
N_FEATURES = 213
DEFAULT_OUTPUT = Path("recursos/datos-sinteticos/gcms_features_sinteticas.csv")


def feature_value(group: str, feature_index: int, rng: random.Random) -> float:
    """Devuelve una intensidad simulada con algunas senales diferenciales."""
    baseline = rng.lognormvariate(8.0, 0.35)

    if feature_index in {4, 12, 29, 49, 84, 101, 137, 155, 188, 205}:
        if group == "Good":
            baseline *= 1.45
        elif group == "Bad":
            baseline *= 1.15
        else:
            baseline *= 0.75

    if feature_index in {17, 43, 57, 91, 120, 176}:
        if group == "Bad":
            baseline *= 1.55
        elif group == "Good":
            baseline *= 1.05
        else:
            baseline *= 0.85

    if feature_index in {2, 9, 31, 60, 144}:
        if group == "Culture":
            baseline *= 1.60
        else:
            baseline *= 0.90

    noise = rng.normalvariate(1.0, 0.08)
    return round(max(baseline * noise, 0.0), 3)


def build_rows(seed: int) -> list[dict[str, str | float]]:
    rng = random.Random(seed)
    rows: list[dict[str, str | float]] = []

    for group, count in GROUPS:
        for sample_number in range(1, count + 1):
            row: dict[str, str | float] = {
                "sample_id": f"{group}_{sample_number:03d}",
                "grupo": group,
            }
            for feature_index in range(1, N_FEATURES + 1):
                row[f"feature_{feature_index:03d}"] = feature_value(
                    group, feature_index, rng
                )
            rows.append(row)

    rng.shuffle(rows)
    return rows


def write_csv(rows: list[dict[str, str | float]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["sample_id", "grupo"] + [
        f"feature_{feature_index:03d}" for feature_index in range(1, N_FEATURES + 1)
    ]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Genera datos sinteticos para el curso IA GC-MS."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Ruta del CSV de salida. Por defecto: {DEFAULT_OUTPUT}",
    )
    parser.add_argument("--seed", type=int, default=42, help="Semilla aleatoria.")
    args = parser.parse_args()

    rows = build_rows(args.seed)
    write_csv(rows, args.output)
    print(f"OK: {len(rows)} muestras x {N_FEATURES} features -> {args.output}")


if __name__ == "__main__":
    main()

