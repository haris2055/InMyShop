import { Container } from 'react-bootstrap'
import Header from './components/Header'
import Footer from './components/Footer'
import HomeScreen from './screens/HomeScreen'


function App() {
  return (
    <div>
      <Header />
      <main className="py-3">
        <h1>
          <Container>
            <HomeScreen />
          </Container>
          </h1>
      </main>
      
      <Footer />
    </div>
  );
}

export default App;