import numpy as np

bboxes = {'accidentalDoubleFlat': np.array([0.01302075, 0.01486308]),
 'accidentalDoubleSharp': np.array([0.00904615, 0.00639018]),
 'accidentalFlat': np.array([0.00775975, 0.01524346]),
 'accidentalFlatSmall': np.array([0.00543591, 0.01038759]),
 'accidentalNatural': np.array([0.00603911, 0.01789138]),
 'accidentalNaturalSmall': np.array([0.00428781, 0.01265729]),
 'accidentalSharp': np.array([0.00644343, 0.01242535]),
 'accidentalSharpSmall': np.array([0.00644343, 0.01242535]),
 'arpeggiato': np.array([0.00676142, 0.02631806]),
 'articAccentAbove': np.array([0.01506256, 0.00591683]),
 'articAccentBelow': np.array([0.01506256, 0.00591683]),
 'articMarcatoAbove': np.array([0.00836808, 0.00650852]),
 'articMarcatoBelow': np.array([0.00836809, 0.00650852]),
 'articStaccatissimoAbove': np.array([0.00341418, 0.0062245 ]),
 'articStaccatissimoBelow': np.array([0.00341418, 0.00622451]),
 'articStaccatoAbove': np.array([0.00535572, 0.00317274]),
 'articStaccatoBelow': np.array([0.00330633, 0.00233781]),
 'articTenutoAbove': np.array([0.0100417 , 0.00094669]),
 'articTenutoBelow': np.array([0.01004171, 0.0009467 ]),
 'augmentationDot': np.array([0.00377866, 0.00267178]),
 'barlineDashed': np.array([0.00158994, 0.02254313]),
 'barlineDotted': np.array([0.0037489 , 0.00265074]),
 'barlineHeavy': np.array([0.00502086, 0.02366732]),
 'barlineSingle': np.array([0.00159422, 0.02415309]),
 'beam': np.array([0.01654345, 0.00352401]),
 'brace': np.array([0.01166973, 0.09901859]),
 'cClefAlto': np.array([0.0227612 , 0.02366732]),
 'cClefAltoChange': np.array([0.01837632, 0.01893386]),
 'cClefTenor': np.array([0.0227612 , 0.02366733]),
 'cClefTenorChange': np.array([0.01798238, 0.01817765]),
 'caesura': np.array([0.00384932, 0.00733687]),
 'clef15': np.array([0.01739726, 0.00574051]),
 'clef8': np.array([0.01169108, 0.00578649]),
 'coda': np.array([0.0223428 , 0.02070891]),
 'dynamicFF': np.array([0.02726344, 0.01433696]),
 'dynamicFFF': np.array([0.03918441, 0.01531276]),
 'dynamicFFFF': np.array([0.04975582, 0.01531276]),
 'dynamicFFFFF': np.array([0.06032722, 0.01531276]),
 'dynamicForte': np.array([0.01869229, 0.01433696]),
 'dynamicFortePiano': np.array([0.02593522, 0.01531276]),
 'dynamicMF': np.array([0.02000793, 0.00934782]),
 'dynamicMP': np.array([0.01759092, 0.01229208]),
 'dynamicMezzo': np.array([0.00852606, 0.00836721]),
 'dynamicPP': np.array([0.02868748, 0.01036629]),
 'dynamicPPP': np.array([0.03873041, 0.01017212]),
 'dynamicPPPP': np.array([0.05044499, 0.01017212]),
 'dynamicPPPPP': np.array([0.06554389, 0.01036628]),
 'dynamicPiano': np.array([0.01530114, 0.01017148]),
 'dynamicRinforzando2': np.array([0.02857702, 0.01531276]),
 'dynamicSforzando1': np.array([0.02074784, 0.01531276]),
 'dynamicSforzato': np.array([0.02626492, 0.01531276]),
 'fClef': np.array([0.02178862, 0.01558448]),
 'fClefChange': np.array([0.01269941, 0.01047042]),
 'fermataAbove': np.array([0.01597581, 0.00577767]),
 'fermataBelow': np.array([0.01331599, 0.01661173]),
 'fingering0': np.array([0.00699573, 0.00650851]),
 'fingering1': np.array([0.00655389, 0.00656058]),
 'fingering2': np.array([0.00699572, 0.00650851]),
 'fingering3': np.array([0.00636979, 0.00650851]),
 'fingering4': np.array([0.00767688, 0.00652153]),
 'fingering5': np.array([0.00670117, 0.00650851]),
 'flag128thDown': np.array([0.00947268, 0.0325899 ]),
 'flag128thUp': np.array([0.00746433, 0.0370157 ]),
 'flag16thDown': np.array([0.0067246 , 0.01240878]),
 'flag16thUp': np.array([0.00746434, 0.02075624]),
 'flag32ndDown': np.array([0.0067246 , 0.01552339]),
 'flag32ndUp': np.array([0.00746434, 0.02518203]),
 'flag64thDown': np.array([0.00947268, 0.02667307]),
 'flag64thUp': np.array([0.00746433, 0.03109886]),
 'flag8thDown': np.array([0.01160589, 0.01922727]),
 'flag8thDownSmall': np.array([0.00672459, 0.01161356]),
 'flag8thUp': np.array([0.00894058, 0.01712802]),
 'flag8thUpSmall': np.array([0.00534219, 0.01240877]),
 'gClef': np.array([0.0217094, 0.0357589]),
 'gClefChange': np.array([0.01727173, 0.03547732]),
 'graceNoteAcciaccaturaStemDown': np.array([0.011042  , 0.01665336]),
 'graceNoteAcciaccaturaStemUp': np.array([0.00979401, 0.01603698]),
 'graceNoteAppoggiaturaStemDown': np.array([0.00672459, 0.01161355]),
 'graceNoteAppoggiaturaStemUp': np.array([0.00534219, 0.01240878]),
 'hairpin': np.array([0.15862618, 0.00795093]),
 'keyFlat': np.array([0.00775975, 0.01524346]),
 'keyNatural': np.array([0.00609197, 0.01808183]),
 'keySharp': np.array([0.00920489, 0.01775049]),
 'keyboardPedalPed': np.array([0.02908747, 0.01183366]),
 'keyboardPedalUp': np.array([0.01302075, 0.00920658]),
 'legerLine': np.array([0.01664973, 0.00118978]),
 'noteheadBlack': np.array([0.0086032 , 0.00596491]),
 'noteheadBlackSmall': np.array([0.00761496, 0.00460566]),
 'noteheadDoubleWhole': np.array([0.01968174, 0.00852023]),
 'noteheadHalf': np.array([0.01265256, 0.00622812]),
 'noteheadHalfSmall': np.array([0.00813044, 0.00460567]),
 'noteheadWhole': np.array([0.01477863, 0.00667986]),
 'noteheadWholeSmall': np.array([0.01115299, 0.00460567]),
 'ornamentMordent': np.array([0.01680313, 0.00790488]),
 'ornamentTrill': np.array([0.02004994, 0.01304069]),
 'ornamentTurn': np.array([0.01827591, 0.00624817]),
 'ornamentTurnInverted': np.array([0.01827591, 0.00624817]),
 'repeatDot': np.array([0.0037489 , 0.00265074]),
 'rest128th': np.array([0.01456047, 0.03467263]),
 'rest16th': np.array([0.01091198, 0.01692214]),
 'rest32nd': np.array([0.01271949, 0.02283897]),
 'rest64th': np.array([0.01395797, 0.0287558 ]),
 'rest8th': np.array([0.01022263, 0.01114037]),
 'restDoubleWhole': np.array([0.00502086, 0.00591684]),
 'restHBar': np.array([0.02567497, 0.01185733]),
 'restHalf': np.array([0.01112289, 0.00298316]),
 'restLonga': np.array([0.00502085, 0.01183367]),
 'restMaxima': np.array([0.01506256, 0.01183367]),
 'restQuarter': np.array([0.00853163, 0.01796295]),
 'restWhole': np.array([0.01643043, 0.00422236]),
 'segno': np.array([0.02092022, 0.02218811]),
 'slur': np.array([0.01407261, 0.00254135]),
 'staffLine': np.array([9.0476255e-01, 5.9340000e-04]),
 'stem': np.array([0.00108785, 0.01960778]),
 'stringsDownBow': np.array([0.01201074, 0.00734739]),
 'stringsUpBow': np.array([0.01005393, 0.01221385]),
 'tie': np.array([0.0040899 , 0.00097418]),
 'timeSig0': np.array([0.01228436, 0.01183366]),
 'timeSig1': np.array([0.01071115, 0.01190466]),
 'timeSig2': np.array([0.01228435, 0.01183367]),
 'timeSig3': np.array([0.0111463 , 0.01183367]),
 'timeSig4': np.array([0.01207822, 0.01192759]),
 'timeSig5': np.array([0.01168185, 0.01183367]),
 'timeSig6': np.array([0.0113806 , 0.01183366]),
 'timeSig7': np.array([0.01205005, 0.01190467]),
 'timeSig8': np.array([0.01245171, 0.01183366]),
 'timeSig9': np.array([0.0113806 , 0.01183367]),
 'timeSigCommon': np.array([0.01449353, 0.01242535]),
 'timeSigCutCommon': np.array([0.01449353, 0.01656713]),
 'tuplet3': np.array([0.00736375, 0.00728937]),
 'tuplet6': np.array([0.00730576, 0.00723196]),
 'unpitchedPercussionClef1': np.array([0.00890364, 0.00946692])}
