"""Recreate the portfolio figures from the accompanying CSV dataset.

This script reproduces charts and comparisons; it does not run WITNESS.
"""
from pathlib import Path
import argparse
import csv
import math

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, PercentFormatter

PORTFOLIO = Path(__file__).resolve().parents[1]
DEFINITIONS = [
    ('Original layout', 'H1', '#007F86', '-', 'o'),
    ('Leak Test Moved', 'H1', '#007F86', (0, (5, 3)), 'D'),
    ('Original layout', 'H2', '#B65A16', '-', 'o'),
    ('Leak Test Moved', 'H2', '#B65A16', (0, (5, 3)), 'D'),
]


def read_capacity_data(path):
    series = {(layout, availability): {} for layout, availability, *_ in DEFINITIONS}
    with path.open(encoding='utf-8-sig', newline='') as handle:
        for row in csv.DictReader(handle):
            key = (row['layout'], row['availability_scenario'])
            if key not in series:
                raise ValueError(f'Unknown scenario: {key}')
            pallets = int(row['pallets'])
            capacity = float(row['annual_capacity_thousand_units'])
            if pallets in series[key]:
                raise ValueError(f'Duplicate pallet quantity: {key}, {pallets}')
            if not math.isfinite(capacity) or capacity <= 0:
                raise ValueError(f'Capacity must be finite and positive: {key}, {pallets}')
            series[key][pallets] = capacity
    for key, points in series.items():
        if sorted(points) != list(range(20, 41, 2)):
            raise ValueError(f'Expected eleven pallet quantities from 20 to 40: {key}')
    return series


def figure_axes():
    fig, ax = plt.subplots(figsize=(13, 7.5), facecolor='white')
    fig.subplots_adjust(left=.105, right=.98, bottom=.14, top=.89)
    ax.set_facecolor('white')
    ax.set_xlim(19.5, 40.5)
    ax.set_xticks(list(range(20, 41, 2)))
    ax.set_xlabel('Pallets in circulation', labelpad=12, color='#122D42', fontsize=12)
    ax.grid(axis='y', color='#DCE6EC', linewidth=.9)
    ax.grid(axis='x', color='#EDF2F5', linewidth=.6)
    ax.set_axisbelow(True)
    ax.tick_params(colors='#536B7B', length=0, pad=8)
    for side in ['top', 'right']:
        ax.spines[side].set_visible(False)
    for side in ['left', 'bottom']:
        ax.spines[side].set_color('#CDDCE5')
    return fig, ax


def save_figure(fig, output, name):
    for extension in ['png', 'svg', 'pdf']:
        fig.savefig(output / f'{name}.{extension}', dpi=200, facecolor='white',
                    metadata={'Creator': 'Python / Matplotlib'})
    plt.close(fig)


def create_figures(series, output):
    output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'svg.fonttype': 'none'})
    fig, ax = figure_axes()
    all_capacities = []
    for layout, availability, color, style, marker in DEFINITIONS:
        points = series[(layout, availability)]
        pallets = sorted(points)
        capacities = [points[n] for n in pallets]
        all_capacities.extend(capacities)
        ax.plot(pallets, capacities, color=color, linestyle=style, marker=marker,
                markersize=6, linewidth=2.7, label=f'{availability} · {layout}', zorder=3)
    ax.set_ylim(math.floor(min(all_capacities) / 10) * 10 - 5,
                math.ceil(max(all_capacities) / 10) * 10)
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.set_ylabel('Annual production capacity\n(thousand units / year)',
                  labelpad=12, color='#122D42', fontsize=12)
    ax.legend(loc='lower center', bbox_to_anchor=(.5, 1.015), ncol=2, frameon=False,
              fontsize=11, columnspacing=3, handlelength=3)
    save_figure(fig, output, 'production-capacity')

    fig, ax = figure_axes()
    comparisons = []
    for availability, color, marker in [('H1', '#007F86', 'o'), ('H2', '#B65A16', 's')]:
        original = series[('Original layout', availability)]
        moved = series[('Leak Test Moved', availability)]
        pallets = sorted(original)
        changes = [(moved[n] / original[n] - 1) * 100 for n in pallets]
        ax.plot(pallets, changes, color=color, marker=marker, markersize=6,
                linewidth=2.7, label=availability)
        comparisons.extend((availability, n, original[n], moved[n], change)
                           for n, change in zip(pallets, changes))
    ax.axhline(0, color='#6E8594', linewidth=1.2, linestyle=(0, (4, 4)), zorder=2)
    ax.margins(y=.15)
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    ax.set_ylabel('Capacity change with station relocation\n(% relative to the original layout)',
                  labelpad=12, color='#122D42', fontsize=12)
    ax.legend(loc='lower center', bbox_to_anchor=(.5, 1.015), ncol=2, frameon=False,
              fontsize=11, handlelength=3, columnspacing=3)
    save_figure(fig, output, 'layout-capacity-change')

    with (output / 'layout-capacity-change-data.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['availability_scenario', 'pallets', 'original_capacity_thousand_units',
                         'relocated_capacity_thousand_units', 'relative_capacity_change_percent'])
        writer.writerows(comparisons)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=PORTFOLIO / 'data/capacity-scenarios.csv')
    parser.add_argument('--output', type=Path, default=PORTFOLIO / 'reproduced-figures')
    args = parser.parse_args()
    create_figures(read_capacity_data(args.data), args.output)
    print(f'Created two figures in PNG, SVG and PDF, plus comparison data, in {args.output}')
