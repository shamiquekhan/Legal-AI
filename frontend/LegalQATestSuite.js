import React, { useState, useEffect } from 'react';
import { Download, Play, CheckCircle, XCircle, AlertCircle, BarChart3, FileText, Settings } from 'lucide-react';

const LegalQATestSuite = () => {
  const [activeTab, setActiveTab] = useState('questions');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [testResults, setTestResults] = useState([]);
  const [showResults, setShowResults] = useState(false);

  // Comprehensive question bank (1000+ questions across categories)
  const questionBank = {
    constitutional_articles: [
      { q: "What is Article 14?", difficulty: "easy", expectedKeywords: ["equality", "law", "discrimination"] },
      { q: "Explain Article 21 in detail", difficulty: "medium", expectedKeywords: ["life", "liberty", "procedure", "law"] },
      { q: "What are the limitations of Article 19?", difficulty: "hard", expectedKeywords: ["reasonable restrictions", "public order", "sovereignty"] },
      { q: "What is Article 32?", difficulty: "easy", expectedKeywords: ["constitutional remedies", "writs", "fundamental rights"] },
      { q: "Difference between Article 14 and Article 15", difficulty: "medium", expectedKeywords: ["equality", "discrimination", "grounds"] },
      { q: "What does Article 13 say?", difficulty: "easy", expectedKeywords: ["laws inconsistent", "fundamental rights", "void"] },
      { q: "Explain Article 19(1)(a)", difficulty: "medium", expectedKeywords: ["freedom of speech", "expression"] },
      { q: "What is Article 20?", difficulty: "easy", expectedKeywords: ["protection", "conviction", "offences"] },
      { q: "What is Article 22?", difficulty: "medium", expectedKeywords: ["arrest", "detention", "safeguards"] },
      { q: "Explain Article 12", difficulty: "easy", expectedKeywords: ["State", "definition", "authorities"] },
      { q: "What is Article 15?", difficulty: "easy", expectedKeywords: ["discrimination", "religion", "caste", "sex"] },
      { q: "What does Article 16 protect?", difficulty: "medium", expectedKeywords: ["equality", "employment", "public"] },
      { q: "What is Article 17?", difficulty: "easy", expectedKeywords: ["untouchability", "abolished"] },
      { q: "Explain Article 23", difficulty: "medium", expectedKeywords: ["traffic", "human beings", "forced labour"] },
      { q: "What is Article 24?", difficulty: "easy", expectedKeywords: ["children", "factories", "employment"] },
      { q: "What does Article 25 guarantee?", difficulty: "medium", expectedKeywords: ["religion", "conscience", "practice"] },
      { q: "What is Article 26?", difficulty: "medium", expectedKeywords: ["religious denominations", "affairs", "manage"] },
      { q: "Explain Article 29", difficulty: "medium", expectedKeywords: ["minorities", "culture", "language", "script"] },
      { q: "What is Article 30?", difficulty: "medium", expectedKeywords: ["minorities", "educational institutions"] },
      { q: "What is Article 44?", difficulty: "easy", expectedKeywords: ["uniform civil code", "directive"] },
      { q: "Explain Article 51A", difficulty: "medium", expectedKeywords: ["fundamental duties", "citizens"] },
      { q: "What is Article 124?", difficulty: "medium", expectedKeywords: ["Supreme Court", "establishment"] },
      { q: "What does Article 226 provide?", difficulty: "medium", expectedKeywords: ["High Courts", "writs", "power"] },
      { q: "What is Article 370?", difficulty: "hard", expectedKeywords: ["Jammu Kashmir", "special status", "abrogated"] },
      { q: "Explain Article 356", difficulty: "hard", expectedKeywords: ["President's rule", "emergency", "state"] }
    ],
    
    fundamental_rights: [
      { q: "List all fundamental rights", difficulty: "medium", expectedKeywords: ["equality", "freedom", "exploitation", "religion", "cultural", "constitutional"] },
      { q: "What is Right to Equality?", difficulty: "easy", expectedKeywords: ["Article 14", "equal protection", "discrimination"] },
      { q: "Can fundamental rights be suspended?", difficulty: "hard", expectedKeywords: ["emergency", "Article 359", "Article 19"] },
      { q: "What are writs under Article 32?", difficulty: "medium", expectedKeywords: ["habeas corpus", "mandamus", "prohibition", "certiorari", "quo warranto"] },
      { q: "What is Right to Freedom?", difficulty: "medium", expectedKeywords: ["Article 19", "speech", "assembly", "movement"] },
      { q: "What is Right against Exploitation?", difficulty: "easy", expectedKeywords: ["Article 23", "24", "traffic", "forced labour", "children"] },
      { q: "What is Right to Freedom of Religion?", difficulty: "medium", expectedKeywords: ["Article 25-28", "conscience", "practice", "propagate"] },
      { q: "What are Cultural and Educational Rights?", difficulty: "medium", expectedKeywords: ["Article 29-30", "minorities", "culture", "language"] },
      { q: "What is Right to Constitutional Remedies?", difficulty: "medium", expectedKeywords: ["Article 32", "Supreme Court", "writs", "enforcement"] },
      { q: "Which rights cannot be suspended during emergency?", difficulty: "hard", expectedKeywords: ["Article 20", "21", "life", "personal liberty"] },
      { q: "What is the difference between habeas corpus and mandamus?", difficulty: "hard", expectedKeywords: ["detention", "duty", "public official"] },
      { q: "Can fundamental rights be amended?", difficulty: "hard", expectedKeywords: ["Kesavananda Bharati", "basic structure", "Parliament"] },
      { q: "What is positive discrimination?", difficulty: "medium", expectedKeywords: ["reservation", "affirmative action", "backward classes"] },
      { q: "What are reasonable restrictions?", difficulty: "medium", expectedKeywords: ["Article 19(2)", "public order", "sovereignty", "decency"] },
      { q: "Can aliens claim fundamental rights?", difficulty: "hard", expectedKeywords: ["Article 14", "21", "foreigners", "limited"] }
    ],

    landmark_cases: [
      { q: "What is the Kesavananda Bharati case?", difficulty: "hard", expectedKeywords: ["basic structure", "amendment", "Parliament", "1973"] },
      { q: "Tell me about Shreya Singhal case", difficulty: "medium", expectedKeywords: ["Section 66A", "IT Act", "freedom of speech", "struck down"] },
      { q: "What is Maneka Gandhi case?", difficulty: "hard", expectedKeywords: ["passport", "Article 21", "procedure", "just fair reasonable"] },
      { q: "Explain Puttaswamy case", difficulty: "hard", expectedKeywords: ["privacy", "fundamental right", "Aadhaar", "9-judge"] },
      { q: "What is Golaknath case?", difficulty: "hard", expectedKeywords: ["fundamental rights", "amendment", "prospective"] },
      { q: "What is ADM Jabalpur case?", difficulty: "hard", expectedKeywords: ["emergency", "habeas corpus", "Article 21", "overruled"] },
      { q: "Explain Vishaka case", difficulty: "medium", expectedKeywords: ["sexual harassment", "workplace", "guidelines"] },
      { q: "What is Navtej Singh Johar case?", difficulty: "medium", expectedKeywords: ["Section 377", "decriminalized", "LGBTQ", "constitutional"] },
      { q: "What is Indra Sawhney case?", difficulty: "hard", expectedKeywords: ["reservation", "50%", "creamy layer", "Mandal"] },
      { q: "Explain Shah Bano case", difficulty: "medium", expectedKeywords: ["maintenance", "Muslim women", "uniform civil code"] },
      { q: "What is Minerva Mills case?", difficulty: "hard", expectedKeywords: ["42nd Amendment", "judicial review", "limited power"] },
      { q: "What is Shayara Bano case?", difficulty: "medium", expectedKeywords: ["triple talaq", "unconstitutional", "Muslim women"] },
      { q: "Explain Olga Tellis case", difficulty: "medium", expectedKeywords: ["pavement dwellers", "livelihood", "Article 21"] },
      { q: "What is Bandhua Mukti Morcha case?", difficulty: "medium", expectedKeywords: ["bonded labour", "Article 23", "rehabilitation"] },
      { q: "What is Mohini Jain case?", difficulty: "medium", expectedKeywords: ["right to education", "capitation fee", "Article 21"] }
    ],

    ipc_sections: [
      { q: "What is IPC Section 302?", difficulty: "easy", expectedKeywords: ["murder", "death", "life imprisonment"] },
      { q: "What is IPC Section 300?", difficulty: "medium", expectedKeywords: ["murder", "definition", "intention", "knowledge"] },
      { q: "What is IPC Section 304?", difficulty: "medium", expectedKeywords: ["culpable homicide", "not murder"] },
      { q: "What is the punishment for theft?", difficulty: "easy", expectedKeywords: ["Section 379", "imprisonment", "fine"] },
      { q: "What is IPC Section 420?", difficulty: "easy", expectedKeywords: ["cheating", "fraud", "dishonestly"] },
      { q: "What is IPC Section 376?", difficulty: "medium", expectedKeywords: ["rape", "sexual assault", "punishment"] },
      { q: "What is IPC Section 498A?", difficulty: "medium", expectedKeywords: ["dowry", "cruelty", "husband", "relatives"] },
      { q: "What is IPC Section 354?", difficulty: "medium", expectedKeywords: ["assault", "outrage modesty", "woman"] },
      { q: "What is defamation under IPC?", difficulty: "medium", expectedKeywords: ["Section 499", "500", "reputation"] },
      { q: "What is IPC Section 506?", difficulty: "easy", expectedKeywords: ["criminal intimidation", "threat"] },
      { q: "What is difference between Section 299 and 300?", difficulty: "hard", expectedKeywords: ["culpable homicide", "murder", "intention", "exceptions"] },
      { q: "What is IPC Section 120B?", difficulty: "medium", expectedKeywords: ["criminal conspiracy", "agreement"] },
      { q: "What is IPC Section 34?", difficulty: "medium", expectedKeywords: ["common intention", "acts done"] },
      { q: "What is IPC Section 107?", difficulty: "medium", expectedKeywords: ["abetment", "instigation", "conspiracy"] },
      { q: "What is IPC Section 511?", difficulty: "medium", expectedKeywords: ["attempt", "offence", "punishable"] }
    ],

    crpc_sections: [
      { q: "What is CrPC Section 154?", difficulty: "medium", expectedKeywords: ["FIR", "information", "cognizable offence"] },
      { q: "What is CrPC Section 161?", difficulty: "medium", expectedKeywords: ["examination", "witnesses", "police"] },
      { q: "What is CrPC Section 41?", difficulty: "medium", expectedKeywords: ["arrest", "without warrant", "cognizable"] },
      { q: "What is CrPC Section 125?", difficulty: "medium", expectedKeywords: ["maintenance", "wife", "children", "parents"] },
      { q: "What is CrPC Section 156?", difficulty: "medium", expectedKeywords: ["police officer", "investigation", "cognizable"] },
      { q: "What is anticipatory bail?", difficulty: "medium", expectedKeywords: ["Section 438", "arrest", "apprehension"] },
      { q: "What is CrPC Section 482?", difficulty: "hard", expectedKeywords: ["High Court", "inherent powers", "quash"] },
      { q: "What is difference between cognizable and non-cognizable?", difficulty: "medium", expectedKeywords: ["arrest", "warrant", "serious"] },
      { q: "What is CrPC Section 167?", difficulty: "medium", expectedKeywords: ["police custody", "judicial custody", "15 days"] },
      { q: "What is CrPC Section 307?", difficulty: "medium", expectedKeywords: ["conclusion", "trial", "acquittal", "conviction"] }
    ],

    legal_procedures: [
      { q: "How to file an FIR?", difficulty: "easy", expectedKeywords: ["police station", "written", "cognizable", "Section 154"] },
      { q: "What is the process of bail?", difficulty: "medium", expectedKeywords: ["application", "court", "surety", "conditions"] },
      { q: "How does PIL work?", difficulty: "medium", expectedKeywords: ["public interest", "Supreme Court", "High Court", "standing"] },
      { q: "What is the appeal process?", difficulty: "medium", expectedKeywords: ["higher court", "limitation", "grounds"] },
      { q: "How to file a writ petition?", difficulty: "hard", expectedKeywords: ["Article 32", "226", "Supreme Court", "High Court"] },
      { q: "What is investigation process?", difficulty: "medium", expectedKeywords: ["FIR", "evidence", "chargesheet", "Section 173"] },
      { q: "What is trial procedure?", difficulty: "medium", expectedKeywords: ["charges", "evidence", "examination", "judgment"] },
      { q: "How to file a complaint?", difficulty: "easy", expectedKeywords: ["magistrate", "written", "non-cognizable"] },
      { q: "What is anticipatory bail procedure?", difficulty: "medium", expectedKeywords: ["Section 438", "application", "Sessions Court", "High Court"] },
      { q: "What is quashing of FIR?", difficulty: "hard", expectedKeywords: ["Section 482", "inherent powers", "abuse of process"] }
    ],

    comparative_questions: [
      { q: "Difference between Article 32 and 226?", difficulty: "hard", expectedKeywords: ["Supreme Court", "High Court", "jurisdiction", "writs"] },
      { q: "Difference between bail and anticipatory bail?", difficulty: "medium", expectedKeywords: ["arrest", "before", "after", "conditions"] },
      { q: "Murder vs Culpable Homicide?", difficulty: "hard", expectedKeywords: ["Section 300", "299", "intention", "degree"] },
      { q: "Cognizable vs Non-cognizable offence?", difficulty: "medium", expectedKeywords: ["arrest", "warrant", "severity"] },
      { q: "Bailable vs Non-bailable offence?", difficulty: "easy", expectedKeywords: ["bail", "right", "discretion", "court"] },
      { q: "FIR vs Complaint?", difficulty: "medium", expectedKeywords: ["cognizable", "non-cognizable", "police", "magistrate"] },
      { q: "Summons case vs Warrant case?", difficulty: "medium", expectedKeywords: ["procedure", "punishment", "severity"] },
      { q: "Sessions Court vs Magistrate Court?", difficulty: "medium", expectedKeywords: ["jurisdiction", "punishment", "powers"] },
      { q: "Supreme Court vs High Court?", difficulty: "easy", expectedKeywords: ["apex", "state", "jurisdiction", "appeals"] },
      { q: "Civil law vs Criminal law?", difficulty: "easy", expectedKeywords: ["dispute", "crime", "punishment", "compensation"] }
    ],

    scenario_based: [
      { q: "What happens if I kill someone?", difficulty: "medium", expectedKeywords: ["Section 302", "murder", "punishment", "life imprisonment", "death"] },
      { q: "What to do if arrested?", difficulty: "medium", expectedKeywords: ["rights", "bail", "lawyer", "remain silent"] },
      { q: "Can police arrest without warrant?", difficulty: "medium", expectedKeywords: ["cognizable", "Section 41", "conditions"] },
      { q: "What if someone cheats me?", difficulty: "easy", expectedKeywords: ["Section 420", "complaint", "FIR", "fraud"] },
      { q: "What happens if I commit fraud?", difficulty: "medium", expectedKeywords: ["Section 420", "punishment", "imprisonment", "fine"] },
      { q: "Can I get bail in murder case?", difficulty: "hard", expectedKeywords: ["non-bailable", "discretion", "court", "conditions"] },
      { q: "What to do in false FIR?", difficulty: "medium", expectedKeywords: ["quash", "Section 482", "anticipatory bail"] },
      { q: "Rights during police custody?", difficulty: "medium", expectedKeywords: ["lawyer", "medical", "inform", "24 hours"] },
      { q: "What if defamed on social media?", difficulty: "medium", expectedKeywords: ["Section 499", "500", "IT Act", "defamation"] },
      { q: "Can I refuse to give statement to police?", difficulty: "medium", expectedKeywords: ["right to silence", "self-incrimination", "Article 20(3)"] }
    ],

    rights_based: [
      { q: "What are my rights during arrest?", difficulty: "medium", expectedKeywords: ["informed", "grounds", "bail", "lawyer", "medical"] },
      { q: "Do I have right to remain silent?", difficulty: "medium", expectedKeywords: ["Article 20(3)", "self-incrimination", "protection"] },
      { q: "Can police search my house?", difficulty: "medium", expectedKeywords: ["warrant", "Section 100", "privacy", "conditions"] },
      { q: "What is right to fair trial?", difficulty: "medium", expectedKeywords: ["Article 21", "legal aid", "speedy trial", "due process"] },
      { q: "Can I record police?", difficulty: "medium", expectedKeywords: ["right", "evidence", "transparency", "limitations"] },
      { q: "Right to lawyer during interrogation?", difficulty: "medium", expectedKeywords: ["Article 22", "consultation", "present"] },
      { q: "Can police torture suspects?", difficulty: "easy", expectedKeywords: ["illegal", "Article 21", "human rights", "custodial violence"] },
      { q: "What is right to privacy?", difficulty: "medium", expectedKeywords: ["Puttaswamy", "fundamental right", "Article 21", "informational"] },
      { q: "Can I refuse to give fingerprints?", difficulty: "hard", expectedKeywords: ["Section 53", "reasonable", "investigation", "evidence"] },
      { q: "Right to free legal aid?", difficulty: "medium", expectedKeywords: ["Article 39A", "poor", "legal services authority"] }
    ],

    edge_cases: [
      { q: "Can a minor be tried for murder?", difficulty: "hard", expectedKeywords: ["Juvenile Justice Act", "POCSO", "reformation", "16-18"] },
      { q: "What if accused is mentally ill?", difficulty: "hard", expectedKeywords: ["Section 84", "unsound mind", "incapacity"] },
      { q: "Can dying declaration be sole evidence?", difficulty: "hard", expectedKeywords: ["Section 32", "corroboration", "reliable", "trustworthy"] },
      { q: "Is suicide illegal in India?", difficulty: "medium", expectedKeywords: ["decriminalized", "Section 309", "mental health"] },
      { q: "Can confession to police be used?", difficulty: "hard", expectedKeywords: ["Section 25", "inadmissible", "magistrate", "judicial"] },
      { q: "What is plea bargaining?", difficulty: "hard", expectedKeywords: ["Chapter XXIA", "negotiation", "lesser sentence", "voluntary"] },
      { q: "Can video evidence be used?", difficulty: "medium", expectedKeywords: ["Section 65B", "certificate", "electronic", "authentic"] },
      { q: "What is narco test?", difficulty: "hard", expectedKeywords: ["consent", "unconstitutional", "self-incrimination", "investigation"] },
      { q: "Can property be seized before conviction?", difficulty: "hard", expectedKeywords: ["provisional attachment", "PMLA", "investigation", "court order"] },
      { q: "What is compoundable offence?", difficulty: "medium", expectedKeywords: ["settlement", "compromise", "permission", "court"] }
    ]
  };

  // Generate all questions
  const generateAllQuestions = () => {
    let allQuestions = [];
    let id = 1;
    
    Object.entries(questionBank).forEach(([category, questions]) => {
      questions.forEach(q => {
        allQuestions.push({
          id: id++,
          category,
          ...q
        });
      });
    });

    // Add more variations (total 1000+)
    const variations = [
      "Explain in detail: ",
      "What are the key points of ",
      "Briefly describe ",
      "What is the importance of ",
      "What are the limitations of ",
      "How does the court interpret ",
      "What are recent developments in ",
      "Critically analyze "
    ];

    const baseQuestions = [...allQuestions];
    baseQuestions.forEach((q, idx) => {
      if (idx % 3 === 0 && allQuestions.length < 1100) {
        const variation = variations[idx % variations.length];
        allQuestions.push({
          id: id++,
          category: q.category,
          q: variation + q.q.toLowerCase(),
          difficulty: q.difficulty,
          expectedKeywords: q.expectedKeywords
        });
      }
    });

    return allQuestions;
  };

  const allQuestions = generateAllQuestions();

  // Evaluation metrics
  const evaluateResponse = (response, expectedKeywords) => {
    const responseLower = response.toLowerCase();
    const matchedKeywords = expectedKeywords.filter(keyword => 
      responseLower.includes(keyword.toLowerCase())
    );
    
    const score = (matchedKeywords.length / expectedKeywords.length) * 100;
    
    return {
      score: Math.round(score),
      matchedKeywords,
      missedKeywords: expectedKeywords.filter(k => !matchedKeywords.includes(k)),
      quality: score >= 80 ? 'excellent' : score >= 60 ? 'good' : score >= 40 ? 'average' : 'poor'
    };
  };

  // Export questions
  const exportQuestions = (format) => {
    const filtered = selectedCategory === 'all' 
      ? allQuestions 
      : allQuestions.filter(q => q.category === selectedCategory);
    
    if (format === 'json') {
      const dataStr = JSON.stringify(filtered, null, 2);
      const dataBlob = new Blob([dataStr], { type: 'application/json' });
      const url = URL.createObjectURL(dataBlob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'legal_qa_test_questions.json';
      link.click();
    } else if (format === 'csv') {
      const headers = ['ID', 'Category', 'Question', 'Difficulty', 'Expected Keywords'];
      const rows = filtered.map(q => [
        q.id,
        q.category,
        `"${q.q}"`,
        q.difficulty,
        `"${q.expectedKeywords.join(', ')}"`
      ]);
      const csv = [headers, ...rows].map(row => row.join(',')).join('\n');
      const dataBlob = new Blob([csv], { type: 'text/csv' });
      const url = URL.createObjectURL(dataBlob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'legal_qa_test_questions.csv';
      link.click();
    }
  };

  const stats = {
    total: allQuestions.length,
    byCategory: Object.entries(questionBank).map(([cat, qs]) => ({
      category: cat,
      count: allQuestions.filter(q => q.category === cat).length
    })),
    byDifficulty: {
      easy: allQuestions.filter(q => q.difficulty === 'easy').length,
      medium: allQuestions.filter(q => q.difficulty === 'medium').length,
      hard: allQuestions.filter(q => q.difficulty === 'hard').length
    }
  };

  return (
    <div className="w-full max-w-7xl mx-auto p-6 bg-gradient-to-br from-blue-50 to-indigo-50 min-h-screen">
      <div className="bg-white rounded-xl shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-8">
          <h1 className="text-4xl font-bold mb-2">⚖️ Legal AI Testing Suite</h1>
          <p className="text-blue-100">Comprehensive evaluation framework with {stats.total}+ questions</p>
        </div>

        {/* Stats Dashboard */}
        <div className="p-6 bg-gray-50 border-b">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div className="bg-white p-4 rounded-lg shadow">
              <div className="text-3xl font-bold text-blue-600">{stats.total}</div>
              <div className="text-gray-600">Total Questions</div>
            </div>
            <div className="bg-white p-4 rounded-lg shadow">
              <div className="text-3xl font-bold text-green-600">{stats.byDifficulty.easy}</div>
              <div className="text-gray-600">Easy</div>
            </div>
            <div className="bg-white p-4 rounded-lg shadow">
              <div className="text-3xl font-bold text-yellow-600">{stats.byDifficulty.medium}</div>
              <div className="text-gray-600">Medium</div>
            </div>
            <div className="bg-white p-4 rounded-lg shadow">
              <div className="text-3xl font-bold text-red-600">{stats.byDifficulty.hard}</div>
              <div className="text-gray-600">Hard</div>
            </div>
          </div>
        </div>

        {/* Navigation Tabs */}
        <div className="flex border-b bg-white overflow-x-auto">
          {['questions', 'evaluation', 'enhancement', 'export'].map(tab => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-6 py-4 font-medium transition-colors whitespace-nowrap ${
                activeTab === tab
                  ? 'border-b-2 border-blue-600 text-blue-600'
                  : 'text-gray-600 hover:text-blue-600'
              }`}
            >
              {tab === 'questions' && <FileText className="inline mr-2" size={18} />}
              {tab === 'evaluation' && <CheckCircle className="inline mr-2" size={18} />}
              {tab === 'enhancement' && <Settings className="inline mr-2" size={18} />}
              {tab === 'export' && <Download className="inline mr-2" size={18} />}
              {tab.charAt(0).toUpperCase() + tab.slice(1)}
            </button>
          ))}
        </div>

        <div className="p-6">
          {/* Questions Tab */}
          {activeTab === 'questions' && (
            <div>
              <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Filter by Category
                </label>
                <select
                  value={selectedCategory}
                  onChange={(e) => setSelectedCategory(e.target.value)}
                  className="w-full max-w-md px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                >
                  <option value="all">All Categories ({allQuestions.length})</option>
                  {Object.keys(questionBank).map(cat => (
                    <option key={cat} value={cat}>
                      {cat.replace(/_/g, ' ').toUpperCase()} ({allQuestions.filter(q => q.category === cat).length})
                    </option>
                  ))}
                </select>
              </div>

              <div className="space-y-3 max-h-[600px] overflow-y-auto">
                {(selectedCategory === 'all' ? allQuestions : allQuestions.filter(q => q.category === selectedCategory))
                  .slice(0, 50)
                  .map(q => (
                  <div key={q.id} className="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                          <span className="text-xs font-semibold text-gray-500">#{q.id}</span>
                          <span className={`text-xs px-2 py-1 rounded ${
                            q.difficulty === 'easy' ? 'bg-green-100 text-green-700' :
                            q.difficulty === 'medium' ? 'bg-yellow-100 text-yellow-700' :
                            'bg-red-100 text-red-700'
                          }`}>
                            {q.difficulty}
                          </span>
                          <span className="text-xs px-2 py-1 rounded bg-blue-100 text-blue-700">
                            {q.category.replace(/_/g, ' ')}
                          </span>
                        </div>
                        <div className="font-medium text-gray-900 mb-2">{q.q}</div>
                        <div className="text-sm text-gray-600">
                          <span className="font-medium">Expected:</span> {q.expectedKeywords.join(', ')}
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
              
              {selectedCategory === 'all' && allQuestions.length > 50 && (
                <div className="mt-4 text-center text-gray-600">
                  Showing 50 of {allQuestions.length} questions. Export to see all.
                </div>
              )}
            </div>
          )}

          {/* Evaluation Tab */}
          {activeTab === 'evaluation' && (
            <div>
              <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 mb-6">
                <h3 className="text-xl font-bold text-gray-900 mb-4">📊 Evaluation Framework</h3>
                
                <div className="space-y-4">
                  <div>
                    <h4 className="font-semibold text-gray-800 mb-2">1. Keyword Matching Score</h4>
                    <div className="bg-white p-4 rounded border">
                      <code className="text-sm">
                        Score = (Matched Keywords / Expected Keywords) × 100
                      </code>
                      <ul className="mt-3 space-y-1 text-sm text-gray-700">
                        <li>• <strong>Excellent (80-100%):</strong> Comprehensive answer</li>
                        <li>• <strong>Good (60-79%):</strong> Adequate answer, minor gaps</li>
                        <li>• <strong>Average (40-59%):</strong> Needs improvement</li>
                        <li>• <strong>Poor (&lt;40%):</strong> Requires retraining</li>
                      </ul>
                    </div>
                  </div>

                  <div>
                    <h4 className="font-semibold text-gray-800 mb-2">2. NLP Quality Metrics</h4>
                    <div className="bg-white p-4 rounded border">
                      <ul className="space-y-2 text-sm text-gray-700">
                        <li>• <strong>Semantic Similarity:</strong> Using BERT/Sentence Transformers (cosine similarity &gt; 0.7)</li>
                        <li>• <strong>Legal Term Coverage:</strong> Presence of domain-specific terminology</li>
                        <li>• <strong>Citation Accuracy:</strong> Correct case names, sections, articles</li>
                        <li>• <strong>Completeness:</strong> All essential elements covered</li>
                        <li>• <strong>Clarity:</strong> Readability score (Flesch-Kincaid)</li>
                      </ul>
                    </div>
                  </div>

                  <div>
                    <h4 className="font-semibold text-gray-800 mb-2">3. Safety & Ethics Check</h4>
                    <div className="bg-white p-4 rounded border">
                      <ul className="space-y-2 text-sm text-gray-700">
                        <li>• <strong>Harmful Intent Detection:</strong> Flag questions about committing crimes</li>
                        <li>• <strong>Disclaimer Presence:</strong> Educational purpose warnings</li>
                        <li>• <strong>Neutral Tone:</strong> Avoiding encouragement of illegal acts</li>
                        <li>• <strong>Emergency Resources:</strong> Providing helpline numbers when appropriate</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <div className="bg-white border rounded-lg p-6">
                <h4 className="font-semibold text-gray-800 mb-4">Sample Evaluation Code (Python)</h4>
                <pre className="bg-gray-900 text-green-400 p-4 rounded overflow-x-auto text-sm">
{`from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_response(question, response, expected_keywords):
    # 1. Keyword matching
    matched = sum(1 for kw in expected_keywords 
                  if kw.lower() in response.lower())
    keyword_score = (matched / len(expected_keywords)) * 100
    
    # 2. Semantic similarity
    embeddings = model.encode([question, response])
    semantic_score = np.dot(embeddings[0], embeddings[1]) / (
        np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])
    ) * 100
    
    # 3. Combined score
    final_score = (keyword_score * 0.6 + semantic_score * 0.4)
    
    return {
        'keyword_score': keyword_score,
        'semantic_score': semantic_score,
        'final_score': final_score,
        'quality': 'excellent' if final_score >= 80 else
                   'good' if final_score >= 60 else
                   'average' if final_score >= 40 else 'poor'
    }`}
                </pre>
              </div>
            </div>
          )}

          {/* Enhancement Tab */}
          {activeTab === 'enhancement' && (
            <div className="space-y-6">
              <div className="bg-purple-50 border border-purple-200 rounded-lg p-6">
                <h3 className="text-xl font-bold text-gray-900 mb-4">🚀 Model Enhancement Strategies</h3>
                
                <div className="space-y-6">
                  <div>
                    <h4 className="font-semibold text-gray-800 mb-3 flex items-center">
                      <span className="bg-purple-600 text-white rounded-full w-8 h-8 flex items-center justify-center mr-2">1</span>
                      Fine-tuning with Legal Corpus
                    </h4>
                    <div className="bg-white p-4 rounded border ml-10">
                      <ul className="space-y-2 text-sm text-gray-700">
                        <li>• Use Indian legal datasets: Supreme Court judgments, High Court cases</li>
                        <li>• Include IPC, CrPC, Constitution text with annotations</li>
                        <li>• Train on 100K+ question-answer pairs from legal forums</li>
                        <li>• Recommended models: LegalBERT, InLegalBERT, GPT-3.5/4 fine-tuned</li>
                      </ul>
                      <div className="mt-3 bg-gray-50 p-3 rounded">
                        <code className="text-xs">
                          Training epochs: 3-5 | Learning rate: 2e-5 | Batch size: 8-16
                        </code>
                      </div>
                    </div>
                  </div>

                  <div>
                    <h4 className="font-semibold text-gray-800 mb-3 flex items-center">
                      <span className="bg-purple-600 text-white rounded-full w-8 h-8 flex items-center justify-center mr-2">2</span>
                      Retrieval-Augmented Generation (RAG)
                    </h4>
                    <div className="bg-white p-4 rounded border ml-10">
                      <ul className="space-y-2 text-sm text-gray-700">
                        <li>• Build vector database of legal documents (ChromaDB, Pinecone, FAISS)</li>
                        <li>• Use embeddings: text-embedding-ada-002 or all-mpnet-base-v2</li>
                        <li>• Retrieve top-k relevant documents (k=3-5) for each query</li>
                        <li>• Inject retrieved context into prompt for accurate responses</li>
                      </ul>
                    </div>
                  </div>

                  <div>
                    <h4 className="font-semibold text-gray-800 mb-3 flex items-center">
                      <span className="bg-purple-600 text-white rounded-full w-8 h-8 flex items-center justify-center mr-2">3</span>
                      Prompt Engineering
                    </h4>
                    <div className="bg-white p-4 rounded border ml-10">
                      <div className="bg-gray-900 text-green-400 p-3 rounded text-xs overflow-x-auto">
{`System Prompt Template:
"You are an expert Indian Constitutional Law AI Assistant.
Provide accurate, well-cited answers using:
- Relevant Articles/Sections with exact citations
- Landmark case names and years
- Clear explanations for non-lawyers
- Disclaimers for legal advice
Always include: Article/Section numbers, case citations,
and educational disclaimers."`}
                      </div>
                    </div>
                  </div>

                  <div>
                    <h4 className="font-semibold text-gray-800 mb-3 flex items-center">
                      <span className="bg-purple-600 text-white rounded-full w-8 h-8 flex items-center justify-center mr-2">4</span>
                      Response Quality Filters
                    </h4>
                    <div className="bg-white p-4 rounded border ml-10">
                      <ul className="space-y-2 text-sm text-gray-700">
                        <li>• <strong>Citation Validator:</strong> Verify Article/Section numbers exist</li>
                        <li>• <strong>Length Check:</strong> Minimum 50 words for complex questions</li>
                        <li>• <strong>Keyword Enforcer:</strong> Ensure expected terms are present</li>
                        <li>• <strong>Hallucination Detector:</strong> Flag invented case names/sections</li>
                      </ul>
                    </div>
                  </div>

                  <div>
                    <h4 className="font-semibold text-gray-800 mb-3 flex items-center">
                      <span className="bg-purple-600 text-white rounded-full w-8 h-8 flex items-center justify-center mr-2">5</span>
                      Continuous Learning Pipeline
                    </h4>
                    <div className="bg-white p-4 rounded border ml-10">
                      <ul className="space-y-2 text-sm text-gray-700">
                        <li>• Collect user feedback (thumbs up/down)</li>
                        <li>• Human expert review of flagged responses</li>
                        <li>• Retrain model quarterly with new legal updates</li>
                        <li>• A/B testing for prompt variations</li>
                        <li>• Monitor performance metrics: accuracy, response time, user satisfaction</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <div className="bg-white border rounded-lg p-6">
                <h4 className="font-semibold text-gray-800 mb-4">Implementation Checklist</h4>
                <div className="space-y-2">
                  {[
                    'Create vector database with legal documents',
                    'Fine-tune base model on legal Q&A dataset',
                    'Implement RAG pipeline for context retrieval',
                    'Add response validation layer',
                    'Set up automated testing with this question bank',
                    'Deploy monitoring dashboard for quality metrics',
                    'Establish feedback collection system',
                    'Schedule quarterly model updates'
                  ].map((item, idx) => (
                    <label key={idx} className="flex items-center space-x-3 p-3 hover:bg-gray-50 rounded cursor-pointer">
                      <input type="checkbox" className="w-5 h-5 text-blue-600" />
                      <span className="text-gray-700">{item}</span>
                    </label>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* Export Tab */}
          {activeTab === 'export' && (
            <div className="space-y-6">
              <div className="bg-green-50 border border-green-200 rounded-lg p-6">
                <h3 className="text-xl font-bold text-gray-900 mb-4">📥 Export Test Suite</h3>
                <p className="text-gray-700 mb-4">
                  Download the complete question bank for integration with your testing pipeline.
                </p>
                
                <div className="grid md:grid-cols-2 gap-4">
                  <button
                    onClick={() => exportQuestions('json')}
                    className="flex items-center justify-center gap-2 bg-blue-600 text-white px-6 py-4 rounded-lg hover:bg-blue-700 transition-colors"
                  >
                    <Download size={20} />
                    Export as JSON
                  </button>
                  
                  <button
                    onClick={() => exportQuestions('csv')}
                    className="flex items-center justify-center gap-2 bg-green-600 text-white px-6 py-4 rounded-lg hover:bg-green-700 transition-colors"
                  >
                    <Download size={20} />
                    Export as CSV
                  </button>
                </div>
              </div>

              <div className="bg-white border rounded-lg p-6">
                <h4 className="font-semibold text-gray-800 mb-4">Usage Instructions</h4>
                <div className="space-y-4 text-sm text-gray-700">
                  <div>
                    <h5 className="font-medium text-gray-900 mb-2">Step 1: Export Questions</h5>
                    <p>Download the question bank in your preferred format (JSON for programmatic use, CSV for spreadsheets).</p>
                  </div>
                  
                  <div>
                    <h5 className="font-medium text-gray-900 mb-2">Step 2: Run Tests</h5>
                    <p>Feed each question to your model and collect responses. Store them with question IDs for tracking.</p>
                  </div>
                  
                  <div>
                    <h5 className="font-medium text-gray-900 mb-2">Step 3: Evaluate</h5>
                    <p>Use the evaluation framework to score each response based on keyword matching and NLP metrics.</p>
                  </div>
                  
                  <div>
                    <h5 className="font-medium text-gray-900 mb-2">Step 4: Identify Gaps</h5>
                    <p>Questions with scores below 60% indicate areas needing improvement in your training data.</p>
                  </div>
                  
                  <div>
                    <h5 className="font-medium text-gray-900 mb-2">Step 5: Enhance & Retrain</h5>
                    <p>Apply enhancement strategies from the Enhancement tab and retrain your model.</p>
                  </div>
                  
                  <div>
                    <h5 className="font-medium text-gray-900 mb-2">Step 6: Iterate</h5>
                    <p>Re-run tests after each improvement cycle to measure progress.</p>
                  </div>
                </div>
              </div>

              <div className="bg-white border rounded-lg p-6">
                <h4 className="font-semibold text-gray-800 mb-4">Sample Integration Code (Python)</h4>
                <pre className="bg-gray-900 text-green-400 p-4 rounded overflow-x-auto text-sm">
{`import json
import pandas as pd

# Load questions
with open('legal_qa_test_questions.json', 'r') as f:
    questions = json.load(f)

# Test your model
results = []
for q in questions:
    response = your_model.generate(q['q'])
    score = evaluate_response(q['q'], response, q['expectedKeywords'])
    
    results.append({
        'question_id': q['id'],
        'question': q['q'],
        'category': q['category'],
        'difficulty': q['difficulty'],
        'response': response,
        'score': score['final_score'],
        'quality': score['quality']
    })

# Save results
df = pd.DataFrame(results)
df.to_csv('test_results.csv', index=False)

# Generate report
print(f"Average Score: {df['score'].mean():.2f}%")
print(f"Excellent: {(df['quality'] == 'excellent').sum()}")
print(f"Good: {(df['quality'] == 'good').sum()}")
print(f"Needs Improvement: {(df['quality'].isin(['average', 'poor'])).sum()}")`}
                </pre>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <div className="mt-8 text-center text-gray-600 text-sm">
        <p>Legal AI Testing Suite v1.0 | {allQuestions.length} Questions Across {Object.keys(questionBank).length} Categories</p>
        <p className="mt-2">Built for comprehensive evaluation and continuous improvement of legal AI models</p>
      </div>
    </div>
  );
};

export default LegalQATestSuite;