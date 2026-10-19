export const BANK_OPTIONS=[
 {id:'physiology',label:'Physiology & foundations',href:'./'},
 {id:'pathology',label:'Pathology & imaging',href:'?bank=pathology'}
];

export function resolveBankConfig(search=''){
 const pathology=new URLSearchParams(search).get('bank')==='pathology';
 return pathology?{
  id:'pathology',dataRoot:'./data/pathology',progressKey:'renal-pathology-picture-quiz-v1',preferencesKey:'renal-pathology-picture-quiz-preferences-v1',exportName:'renal-pathology-progress.json',title:'Renal Pathology & Related · Picture Quiz',brand:'PATHOLOGY PICTURE QUIZ',eyebrow:'Renal · Pathology visual practice',description:'Practice renal pathology, urinalysis, urologic oncology, and imaging using reviewed manual course captures.',footer:'Renal course pathology and imaging · Manual visuals · Local study tool · Not clinical guidance',homeUrl:'?bank=pathology'
 }:{
  id:'physiology',dataRoot:'./data',progressKey:'renal-picture-quiz-v1',preferencesKey:'renal-picture-quiz-preferences-v1',exportName:'renal-progress.json',title:'Renal · Picture Quiz',brand:'PICTURE QUIZ',eyebrow:'Renal · Visual practice',description:'Practice renal anatomy, physiology, fluid balance, acid-base, and dialysis using reviewed course captures.',footer:'Renal course physiology · Manual visuals · Local study tool · Not clinical guidance',homeUrl:'./'
 };
}
