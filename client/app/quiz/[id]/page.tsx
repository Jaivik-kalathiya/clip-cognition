// "use client";
import QuizForm from "@/components/quiz-form";
import { getQuizById } from "@/lib/firebase/quiz.services";
// import { useEffect, useState } from "react";


const Page = async ({ params }: { params: { id: string } }) => {
  // let quizRecord;
  // const [quizData, setQuizData] = useState([]);

  const quizData: any = await getQuizById(params.id);

  // useEffect(() => {
  //   try {
  //     const fetchQuiz = async () => {
  //       const result = await fetch(`http://localhost:5000/api/${params.id}`);
  //       quizRecord = await result.json();
  //       quizRecord = JSON.parse(quizRecord);
  //       setQuizData(quizRecord.questions);
  //       // quizRecord = JSON.stringify(quizRecord);
  //       console.log("Fetcted quiz data: ", quizRecord.questions);
  //     };
  //     fetchQuiz();
  //   } catch (error) {
  //     console.log("Error fetching quiz data: ", error);
  //   }
  // }, []);

  console.log("first", quizData);

  return <QuizForm quizData={quizData.questions} />;
};

export default Page;
