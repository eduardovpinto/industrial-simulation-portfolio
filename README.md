# Industrial Simulation Portfolio

**Eduardo Pinto | WITNESS / Twinn WITNESS | Production capacity and material flow**

I use discrete-event simulation to investigate industrial operating decisions before changes are made to a production system. This portfolio presents the questions studied, the alternatives compared, the available results and the conditions behind the recommendations.

## Featured case study: pallet sizing and layout comparison

**Decision:** how many pallets should circulate through an assembly line, and how does the answer change when the leak-test station is relocated?

The study compares **two layouts**, **two equipment availability assumptions** and **eleven pallet quantities**. It illustrates why layout and pallet quantity should be assessed together.

| Reported comparison | Original layout | Relocated layout |
|---|---:|---:|
| Pallets associated with the highest tested output under both availability assumptions | 30 | 26 |
| Peak output change relative to the original layout under H1 | Reference | −0.22% |
| Peak output change relative to the original layout under H2 | Reference | −1.82% |

H1 and H2 are the higher- and lower-availability assumptions defined in the case study. Each peak comparison allows the layouts to use their own best tested pallet quantity.

The relocated layout reached its highest tested output with four fewer pallets, while its peak output was lower. The study supports a pallet recommendation for either layout. Choosing between layouts also requires the production requirement, implementation costs and other operational considerations.

![Estimated annual production capacity for the tested pallet quantities and scenarios](assets/production-capacity.png)

**[Read the case study](projects/capacidade-linha-montagem.md)** · **[View the result data](data/capacity-scenarios.csv)** · **[Reproduce the figures](scripts/README.md)**

## Industrial decisions addressed

| Decision | What the published case provides |
|---|---|
| Select a circulating pallet quantity | Capacity comparisons over the tested range |
| Assess a layout alternative | Comparisons at equal pallet quantities and at each layout's best tested output |
| Examine availability assumptions | Results under two operating assumptions |
| Interpret the recommendation | Sensitivity around the reported peaks and explicit evidence limits |

## Work presented

- Process modelling and pallet-flow logic in WITNESS 26, as described in the case study.
- Organisation of operating assumptions and process information in Excel.
- Structured comparisons of alternative operating configurations.
- Python figures and derived comparisons based on the published CSV results.

## Evidence and interpretation

The company information used in this case is shared with permission. The figures present simulation estimates, and the case study describes the evidence available and the outstanding checks concerning model configuration, execution settings and annualisation. Post-implementation production improvements and savings have not been established in the published material.

The accompanying Python workflow regenerates charts and comparisons from the stored CSV results. Reproducing the WITNESS experiments is a separate task requiring the model, inputs and execution settings.

## Connecting simulation to business value

A financial assessment would combine the operating results with demand, pallet costs, relocation costs and achievable benefits. This would support a comparison of implementation cost, annual net benefit, ROI and payback. The current case provides the capacity comparison; a numerical investment return remains to be assessed.

## Contact

For a discussion about production capacity, material flow or an industrial simulation study:

[Connect with Eduardo Pinto on LinkedIn](https://www.linkedin.com/in/eduardopinto2407/)
